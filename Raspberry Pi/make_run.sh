#!/bin/bash
#make-run.sh
#make sure a process is always running.


process=python3
makerun="./start_temp.sh"

if ps -a | grep -v grep | grep $process > /dev/null
then
    echo "running"
    exit
else
    echo "starting"
    $makerun &
fi

exit
