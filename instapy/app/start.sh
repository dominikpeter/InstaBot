#!/bin/bash



if [ $(((RANDOM % 3) + 1)) -eq 1 ] || [ $1 -eq 1 ]
then
 echo $(date): Bot started...
 cd ~/Projects/InstaBot/instapy/app
 source ~/Projects/InstaBot/instapy/app/instapy/bin/activate
 python3 ~/Projects/InstaBot/instapy/app/simple_bot.py
else
 echo $(date): Bot not started..
fi
