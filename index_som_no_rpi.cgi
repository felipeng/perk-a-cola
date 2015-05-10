#!/bin/bash

echo -e "Content-Type: text/html\r\n"

ARG=$(echo $QUERY_STRING | cut -f2 -d=)

function play(){
    killall -9 mpg123
    /usr/bin/mpg123 -q songs/$1.mp3
}

if [ "$ARG" == "" ]; then
    perk_on=0
    killall -9 mpg123 2>/dev/null
elif [ "$ARG" == "seq" ]; then
    for i in $(seq 1 12); do killall -9 mpg123; done
    (for perk_seq in $(seq 1 12); do
	play $perk_seq
    done) >&- &
elif [ "$ARG" == "stop" ]; then
    for i in $(seq 1 12); do killall -9 mpg123; done
    echo -n 99 > /dev/rfcomm0
else
    perk_on=$ARG	# marca como ligado para interface web
    echo -n $[$perk_on+1] > /dev/rfcomm0
    play $perk_on >&- &
fi

echo "<html>
<head>
    <!-- iPhone start -->
    <meta content='yes' name='apple-mobile-web-app-capable' />
    <meta content='minimum-scale=0.8, width=device-width, maximum-scale=1.0, user-scalable=no' name='viewport' />
    <link href='imgs/cod_zombies_app.png' rel='apple-touch-icon' />
    <link href='imgs/cod_zombies_startup.png' rel='apple-touch-startup-image' />
    <!-- iPhone end -->
    <title>Perk-A-Cola</title>
</head>
<style type='text/css'>
    button {border: 0px; background-color: transparent; };
</style>
<body style='background-color: black;'>
<form action='index.cgi' method='get' style='width: 400px; margin-left: 10px;'>
<img src='imgs/cod_zombies.png'>"

for perk in $(seq 1 12); do
    if [ "$perk" == "$perk_on" ]; then
	perk_led=${perk}"_on"
    else
	perk_led=${perk}"_off"
    fi
    echo "<button type='submit' name='perk_on' value='"$perk"'><img src='imgs/"${perk_led}".png' width='90px;'></button>"
done

echo "<br />
<button type='submit' name='perk_on' value='seq'><img src='imgs/arrow_switch.png' width='25px;'></button>
<button type='submit' name='perk_on' value='random'><img src='imgs/arrow_switch.png' width='25px;'></button>
<button type='submit' name='perk_on' value='stop'><img src='imgs/arrow_switch.png' width='25px;'></button>
</form>
</body>
</html>"
