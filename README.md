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
	* reboot
	

Enable logging
	
	* find log function in fancontrole.sh
	* uncomment log to file line
	
	
	
## Hardware setup
Get things wired like it is shown in the circuit diagram:
![see repository -> circuit.png](./circuit.png?raw=true "Circuit")