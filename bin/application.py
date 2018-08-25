#!/usr/bin/python3
import signal
import config
from fancontroller import FanController

def main():
    config.init()
       
    # Create controller
    global fc
    fc = FanController()
    fc.setMaximumTemperature(config.MAX_TEMP)
    fc.setMinimumTemperature(config.MIN_TEMP)
    fc.setMinimumSpeed(config.MIN_SPEED)
    fc.setGpioControlPin(config.GPIO_PIN)
    fc.setRefreshRate(config.REFRESH_RATE)
    
    # Initialize signal handling
    registerSignalHandlers()
    
    
    # Wait for controller (infinity)
    try:
        fc.start()
        fc.join()
    except (SystemExit, KeyboardInterrupt, Exception) as e:
        print("Got error or interruption:")
        print(e)
    finally:
        doExit()
        
    
    return 0

def doExit():
    
    fc.stop()
    
    while True:
        try:
            print("Wait for fan controller")
            fc.join(5)
            if not fc.is_alive():
                print("Got fan controller ready for exit")
                break
        except (SystemExit, KeyboardInterrupt, Exception) as e:
            pass
        continue
    
    print("Exit")
    
    return;

def onExit(signal, frame):
    doExit()
    return

def registerSignalHandlers():
    signal.signal(signal.SIGTERM, onExit)
    signal.signal(signal.SIGINT, onExit)
    signal.signal(signal.SIGABRT, onExit)
    return

# Check, that it is run as MAIN module
if __name__ == '__main__':
    print("Starting as main")
    main()
else:
    print("Module mode not implemented. Start as main.")