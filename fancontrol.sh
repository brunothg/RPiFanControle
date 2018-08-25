#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"

function start () {
	
	python3 "${DIR}/bin/application.py" &
	local PID=$!
	echo "$PID" > "${DIR}/pid"

	log "Successfully started"
}

function stop () {
	local PID=$(<"${DIR}/pid")
	kill $PID
	echo "" > "${DIR}/pid"
	
	log "Successfully stopped -> $PID"
}

function restart () {
	stop
	start
}

function install () {
	log "Install default autostart script (/etc/init.d/fancontrol) - change path if not /home/pi/FanControl"

	sudo cp "${DIR}/autostart.sh" "/etc/init.d/fancontrol"
	sudo chmod 755 "/etc/init.d/fancontrol"
	sudo update-rc.d fancontrol defaults
}

function uninstall (){
	sudo update-rc.d fancontrol remove
	sudo rm "/etc/init.d/fancontrol"
}

function log () {
	echo -e "\n $(date) - $1"
#	echo -e "\n $(date) - $1" >> "${DIR}/log.txt"
}




# Actions
case "$1" in
	start)
		start
		;;
	stop)
		stop
		;;
	restart)
		restart
		;;
	install)
		install
		;;
	uninstall)
		uninstall
		;;
	*)
		echo "Usage: $0 {start|stop|restart|install|uninstall}"
		exit 1
		;;
esac

exit 0
