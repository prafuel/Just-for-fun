#!/bin/bash

echo "Welcome here on this Script, here you can do Dictionory Attack on perticular zip file to extract its content : "
read -p "Enter your name of Zip File (Stored at current folder) :" file
read -p "Enter your name of Wordlist File (Stored at ./wordlists folder --> if Empty : default.txt): " list

if [[ ${#list} == 0 ]]
then
    list="default.txt"
fi

verifyPass() {
    password=$1
    comm=$(7z x -p$password -y -oextracted/$file $file | grep Ok)

    if [[ $comm == *"Ok" ]]
    then
        echo $comm
        echo "------- [+] Password : $password -------"
        return 1
    fi
    return 0
}

check=$(file $file | grep zip | awk {'print $11'})
check=${check#*=}
# echo $check #name of Encryption Method

temp=$(7z i | grep $check)
# echo ${#tem}

if [[ ${#temp} != 0 ]]
then
    for item in $(cat ./wordlists/$list)
    do
        verifyPass $item
        if [[ $? == 1 ]]
        then
            echo "-------- All Extracted Files Will be Store in Folder named 'extracted' ---------"
            break
        fi
    done
else
    echo "Zip Encryption is not known"
fi

