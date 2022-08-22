#!/bin/bash

TIMEOUT=3 # seconds

# if $1 is empty, then dont loop
if [ -z $1 ]; then
    loop="false"
    random="false"
    elif [ $1 = "-p" ] && [ $2 !-z ]; then
    loop="false"
    random="false"
    pouet_id=$2
    elif [[ $1 = "-pl" ]]; then
    loop="true"
    random="false"
    pouet_id=$2
    elif [ $1 = "-r" ]; then
    random="true"
    elif [ $1 = "-rl" ]; then
    loop="true"
    random="true"
    elif [ $1 = "-h" ]; then
    echo "Usage: random_demo.sh [-p <pouet_id>] [-r] [-rl]"
    echo " -p <pouet_id> : select demo from pouet id"
    echo " -pl <pouet_id> : loop and select demo from pouet id"
    echo " -r : select random demo"
    echo " -rl : select random demo and loop"
    echo " -h : show this help"
    exit 0
else
    echo "Invalid argument"
    exit 1
fi

play_demo(){
    # if random is enabled, then play a random demo
    if [ $random = "true" ]; then
        echo "Random selection..."
        pouet_id=$(shuf -i0-99999 -n1)
    fi
    
    echo "loop is $loop"
    echo "random is $random"
    echo "pouet_id is $pouet_id"
    
    echo "Selected demo id: $pouet_id"
    chmod +x ~/.showet/data/$pouet_id/*.exe >/dev/null 2>&1
    chmod +x ~/.showet/data/$pouet_id/*.adf >/dev/null 2>&1
    chmod +x ~/.showet/data/$pouet_id/*.dms >/dev/null 2>&1
    chmod +x ~/.showet/data/$pouet_id/*.d64 >/dev/null 2>&1
    chmod +x ~/.showet/data/$pouet_id/*.prg >/dev/null 2>&1
    chmod +x ~/.showet/data/$pouet_id/*.dsk >/dev/null 2>&1
    
    python3 ~/showet/showet.py $pouet_id
    read -p "Press [q] to quit or [enter] to continue (or wait a few seconds)..." -n1 -s -t $TIMEOUT
    # if q is pressed, then quit
    if [[ $REPLY = "q" ]]; then
        echo "Quitting..."
        loop="false"
        exit 0
    fi
}

# if loop is enabled, then loop forever
if [ $loop = "true" ]; then
    while true; do
        play_demo
    done
else
    play_demo
fi
# Cleanup after script
rm -rf ~/.showet/data/* >/dev/null 2>&1
