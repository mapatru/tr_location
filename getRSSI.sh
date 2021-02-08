while read address
do
    read RSSI
    timestamp=`date`
    echo "$timestamp,$address,$RSSI"
done
