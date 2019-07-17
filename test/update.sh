#!/bin/bash

#echo "111"
##exit 0
#a="echo 1"
#echo "$a"
#echo '$a'
#echo `$a`
#b="echo 2222"
#sed test.txt.bak
#sed -i '/server\s\+10.16.42.224:8080/s/^/#/' nginx.conf
#
#if [ $? -eq 0 ]; then
#    echo "$a"
##    exit 1
#else
#    echo `$b`
#fi
#
#
#day=`date +%Y%m%d`
#day2=$(date +%Y%m%d)
#echo $day
#echo ${day2}
#echo ${day}

function isSuccess(){
if [ $1 -eq 0 ];then
 echo $2 "成功"
else
 echo $2 "失败"
fi
}

echo "66666"
#sadsa
isSuccess $? "任务"