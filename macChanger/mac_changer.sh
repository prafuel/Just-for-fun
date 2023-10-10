#!/bin/bash


change_mac() {
    interface=$1
    new_mac=$2
    sudo ifconfig $interface down
    sudo ifconfig $interface hw ether $new_mac
    sudo ifconfig $interface up

    echo "Change Succesful"
}

echo "Enter here Interface Name(Ex. wlo1): "
read interface
# interface=wlo1

echo $interface
mac=$(ifconfig $interface | grep ether | awk '{print $2}')
# echo $mac

echo "Enter Here New Mac Address : "
read new_mac 
# new_mac="b4:b6:b5:b5:9d:ff"
change_mac $interface $new_mac

new_mac=$(ifconfig $interface | grep ether | awk '{print $2}')

echo "Before : $mac, After : $new_mac"
