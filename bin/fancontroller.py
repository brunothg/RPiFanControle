# Controllerclass for the fan
import time
import os
import threading
import RPi.GPIO as GPIO

class FanController (threading.Thread):
    
    running = False
    
    maximumTemperature = 85
    minimumTemperature = 55
    minimumSpeed = 50
    
    refreshRate = 5
    gpioControlPin = 4
    
    fan = None
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "FanController"       
        return
    
    def run(self):
        self.setupGpio()
        
        try:
            while self.running:
                self.adjustFanSpeed()
                time.sleep(2)
                continue
        except (SystemExit, KeyboardInterrupt, Exception) as e:
            print("Fan Controller unplanned interruption:")
            print(e)
        finally:
            self.finishGpio()
            
        return
    
    def adjustFanSpeed(self):
        level = 0
        temp = self.getTemperature()
        maxTemp = self.getMaximumTemperature()
        minTemp = self.getMinimumTemperature()
        minSpeed = self.getMinimumSpeed()
        
        difTemp = maxTemp - minTemp
        relTemp = temp - minTemp
        refSpeed = 100.0 - minSpeed
        
        if temp < minTemp:
            level = 0
        elif temp > maxTemp:
            level = 100
        else:
            level = minSpeed + ((refSpeed/difTemp)*relTemp)
        
        # Level override for testing purposes
        # level = 100
        
        self.fan.ChangeDutyCycle(level)
        print("Set fan speed to "+str(level)+"% by a temperature of "+str(temp)+"°C ["+str(minTemp)+" - "+str(maxTemp)+"]")
        return
        
    def setupGpio(self):
        print("Setup GPIO usage")
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.getGpioControlPin(), GPIO.OUT)
        
        self.fan = GPIO.PWM(self.getGpioControlPin(), 3)
        self.fan.start(0)
        return
    
    def finishGpio(self):
        print("Turn down GPIO usage")
        
        self.fan.ChangeDutyCycle(0)
        self.fan.stop()
        
        GPIO.output(self.getGpioControlPin(), GPIO.LOW)
        GPIO.cleanup()
        return
    
    def start(self):
        print("Start running fan controller")
        print("\tMax-Temp: "+str(self.getMaximumTemperature())+"°C")
        print("\tMin-Temp: "+str(self.getMinimumTemperature())+"°C")
        print("\tMin-Speed: "+str(self.getMinimumSpeed())+"%")
        print("\tRefresh-Rate: "+str(self.getRefreshRate())+"Hz")
        print("\tGpioPin:  "+str(self.getGpioControlPin()))
        
        self.running = True
        super().start()
        return
    
    def stop(self):
        self.running = False
        return
    
    def setMaximumTemperature(self, maxTemp):
        if maxTemp <= self.getMinimumTemperature():
            raise RuntimeError("Maximum temperature has to be higher than the minimum Temperature")
        
        self.maximumTemperature = maxTemp
        return
    
    def getMaximumTemperature(self):
        return self.maximumTemperature
    
    def setMinimumTemperature(self, minTemp):
        if minTemp >= self.getMaximumTemperature():
            raise RuntimeError("Minimum temperature has to be lower than the maximum Temperature")
        
        self.minimumTemperature = minTemp
        return
    
    def getMinimumTemperature(self):
        return self.minimumTemperature
    
    def setMinimumSpeed(self, minSpeed):
        if minSpeed < 0 or minSpeed > 100:
            raise RuntimeError("Minimum speed has to be in range of 0.0 to 100.0")
        
        self.minimumSpeed = minSpeed
        return
    
    def getMinimumSpeed(self):
        return self.minimumSpeed
    
    def setRefreshRate(self, rate):
        if rate < 0 or rate > 19200000:
            raise RuntimeError("Refresh rate has to be in range of 0 to 19200000")
        
        self.refreshRate = rate
        return
    
    def getRefreshRate(self):
        return self.refreshRate
    
    def setGpioControlPin(self, pinNr):
        self.gpioControlPin = pinNr
        return
    
    def getGpioControlPin(self):
        return self.gpioControlPin
    
    def getTemperature(self):
        temp = os.popen('vcgencmd measure_temp').readline()
        temp = temp.replace("temp=","").replace("'C","")
        return float(temp)