#!/bin/bash
### BEGIN INIT INFO
# Provides:             fancontrol
# Required-Start:       $local_fs
# Required-Stop:        $local_fs
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    Automatische Lüftersteuerung für den RasPi
# Description:          Automatische Lüftersteuerung für den RasPi
### END INIT INFO



function start () {
        /home/pi/FanControl/fancontrole.sh start &
}

function stop () {
        /home/pi/FanControl/fancontrole.sh stop
}

function restart () {
	stop
	start
}


# Actions
case "$1" in
        start)
                # START
                start
                ;;
        stop)
                # STOP
                stop
                ;;
        restart)
                # RESTART
		restart
                ;;
esac


exit 0
