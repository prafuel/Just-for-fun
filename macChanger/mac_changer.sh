#!/bin/bash


change_mac() {
    interface=$1
    new_mac=$2
    ifconfig $interface down
    ifconfig $interface hw ether $new_mac
    ifconfig $interface up
}

echo "Enter here Interface Name(Ex. wlo1): "
read interface
# interface=wlo1

echo $interface
mac=$(ifconfig $interface | grep ether | awk '{print $2}')
echo $mac

new_mac="b4:b6:b5:b5:9d:ff"
change_mac $interface $new_mac

new_mac=$(ifconfig $interface | grep ether | awk '{print $2}')

echo "Before : $mac, After : $new_mac"
