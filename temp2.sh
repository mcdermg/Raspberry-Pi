#!/bin/bash
counter=1
#capture user input
echo "Enter the number of seconds to run CPU/GPU temp script:"
read counter

#execute in secongs user input

while [ $counter -gt 0 ];
do
cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuTemp1=$(($cpuTemp0/1000))
cpuTemp2=$(($cpuTemp0/100))
cpuTempM=$(($cpuTemp2 % $cpuTemp1))
cpuFreq=`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq | sed 's/.\{3\}$//'`
dat="$(date)"
echo "${dat}" CPU temp"="$cpuTemp1"."$cpuTempM"'C" /opt/vc/bin/vcgencmd measure_temp|cut -c6-9  CPU frequency=$cpuFreq
echo $cpuTemp1"."$cpuTempM","$cpuFreq>> temprlog.csv
sleep 1
let counter-=1
done
