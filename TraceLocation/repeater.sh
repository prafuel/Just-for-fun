#!/ust/bin/bash
wifi on
data=$(ping -c 3 google.com | grep packets | awk '{print $6}')

if [ "$data" != "100%" ]; then
    echo $data
    python3 send.py
fi
