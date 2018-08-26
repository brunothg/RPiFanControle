# RPiFanControle
Python script for controlling a fan for the Raspberry Pi.
The fan speed will be controlled depending on the SoC's temperature.
All you'll need is a RaspberryPi 3 (other models should work either), a fan and a few electronics.



## Installation
Copy files to /home/pi/FanControle/ (or replace paths in autostart.sh)
	
	* autostart.sh
	* fancontrole.sh
	* bin/ and everything in it
	

Install autostart script

	* Run 'fancontrole.sh install'
	* reboot

	
Change settings
	
	* Edit settings in FanControle/bin/config.py
	*
	* Folgende Werte können angepasst werden
	* MAX_TEMP is the temperature level, that will lead th fan to full speed
	* MIN_TEMP is the temperature level, that the fan will start turning at
	* MIN_SPEED is a procentual value between 0.0 and 100.0 and indicates the minimum speed level to run the fan
	* GPIO_PIN specifies the control pin used for wiring the GPIO-pin with the transistor's base (be carefull, BCM-mode is used for naming the GPIO-pins)
	* REFRESH_RATE is the frequency for PWM (with my fan it has turned out, that higher values than 50Hz does not make any differences)
	*
	* reboot
	

Enable logging
	
	* find log function in fancontrole.sh
	* uncomment log to file line
	
	
	
## Hardware setup
Get things wired like it is shown in the following circuit diagram.

	* The transistor is a 2N2222 NPN transistor with Emitter, Base, Collector (from left to right pin)
	* The fan used is a default 5V and 0.2A fan (otherwise you may need to add resistors). You can order them e.g. on Amazon
	* The blue cable is connected with 5V pin and the 'red'-plus cable of the fan (green in the image)
	* The red cable is connected with the transistor's collector and the 'black'-minus cable of the fan (yellow in the image
	* The black cable is connected with the transistor's emitter and a Pi's ground-connector
	* The other blue cable is connected with the transistor's base and a GPIO-pin an the Pi (GPIO4 is used in the default configuration and on the image)


![see repository -> circuit.png](./circuit.png?raw=true "Circuit")