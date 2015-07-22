#!/bin/bash

# Real Perk-A-Cola Bottles
# Created by Felipe Nogaroto Gonzalez
# License: MIT

# Verify the gpio command
no_gpio(){
echo -e "Content-Type: text/html\r\n
<html>
  <head>
  </head>
  <body>
    Command 'gpio' not found. <br />
    You have to install <a href='http://wiringpi.com'>WiringPi</a> software.
  </body>
</html>
"
  exit
}

GPIO=$(which gpio 2>/dev/null)

# Nao esta funcionando
#if [ -z $GPIO ]; then
#  no_gpio
#fi


# Setup all pins, mode OUT and LOW
for i in $(seq 0 26); do
   gpio -1 mode $i out 1>/dev/null 2>/dev/null
   gpio -1 write $i 0  1>/dev/null 2>/dev/null
done

echo -e 'Content-Type: text/html\r\n'

# Parser pin and value
PIN="${QUERY_STRING/=*}"
VALUE="${QUERY_STRING/*=}"

if [ $VALUE == 0 -o $VALUE == 1 ]; then
   echo "gpio -1 write $PIN $VALUE"
   gpio -1 write $PIN $VALUE
   if [ $PIN == 99 ]; then
      for i in $(seq 0 26); do
         gpio -1 write $i $VALUE 1>/dev/null 2>/dev/null
      done
   fi
fi

# Read pinmap
source pinmap.conf

echo "
<html>
  <head>
	   <!-- iPhone start -->
	   <meta content='yes' name='apple-mobile-web-app-capable' />
	   <meta content='minimum-scale=0.8, width=device-width, maximum-scale=1.0, user-scalable=no' name='viewport' />
	   <link href='imgs/cod_zombies_app.png' rel='apple-touch-icon' />
	   <link href='imgs/cod_zombies_startup.png' rel='apple-touch-startup-image' />
	   <!-- iPhone end -->
     <title>Perk-A-Cola</title>
     <style type='text/css'>
      form  { width: 340px; margin: 5px; }
      body  { background-color: black; }
	    .gray { -webkit-filter: grayscale(90%); }
      .perk { margin-left: 5px; margin-right: 15px;}
	   </style>
     <script>
	    var request = new XMLHttpRequest();
      function led(URI){
    	   request.open('GET', 'index.cgi?' + URI, true);
    	   request.send(null);
         console.log('GET /index.cgi?' + URI);
    	}

    	function player(perk) {
    	   var music = document.getElementById(perk.alt);
    	   if (music.paused == true){
    		     music.play();
    		     perk.className = 'perk';
		         value = 1;
		     } else {
    		     music.pause();
    	    	 perk.className = 'perk gray';
    	    	 value = 0;
    		}
		    led(perk.id + '=' + value);
    	 }
	</script>
    </head>
    <body>
        <form action='index.cgi' method='get'>
          <img src='imgs/cod_zombies.png'>
          <img class='perk gray' onclick='player(this);' id='$deadshot'  src='imgs/deadshot.png'        alt='deadshot_daiquiri' title='Deadshot Daiquiri'>
          <img class='perk gray' onclick='player(this);' id='$double_tap' src='imgs/double_tap.png'      alt='double_tap'        title='Double Tap Root Beer'>
          <img class='perk gray' onclick='player(this);' id='$phd_flooper' src='imgs/phd_flooper.png'     alt='phd_flooper'       title='PhD Flooper'>
          <img class='perk gray' onclick='player(this);' id='$juggernaut' src='imgs/juggernaut.png'      alt='juggernaut'        title='Juggernaut'>
          <img class='perk gray' onclick='player(this);' id='$mule_kick' src='imgs/mule_kick.png'       alt='mule_kick'         title='Mule Kick'>
          <img class='perk gray' onclick='player(this);' id='$quick_revive' src='imgs/quick_revive.png'    alt='quick_revive'      title='Quick Revive'>
          <img class='perk gray' onclick='player(this);' id='$sleight_of_hand' src='imgs/sleight_of_hand.png' alt='sleight_of_hand'   title='Sleight Of Hand'>
          <img class='perk gray' onclick='player(this);' id='$stamin_up' src='imgs/stamin_up.png'       alt='stamin_up'         title='Stamin-Up'>
          <img class='perk gray' onclick='player(this);' id='$whos_who' src='imgs/whos_who.png'        alt='whos_who'          title='Whos Who'>
          <img class='perk gray' onclick='player(this);' id='$tombstone' src='imgs/tombstone.png'       alt='tombstone'         title='Tombstone'>
          <img class='perk gray' onclick='player(this);' id='$vulture_aid' src='imgs/vulture_aid.png'     alt='vulture_aid'       title='Vulture Aid Elixir'>
          <img class='perk gray' onclick='player(this);' id='$electric_cherry' src='imgs/electric_cherry.png' alt='electric_cherry'   title='Electric Cherry'>
          <img class='perk gray' onclick='player(this);' id='99' src='imgs/pack_a_punch.png'    alt='pack_a_punch'      title='Pack A Punch'>
          <audio id='deadshot_daiquiri'>  type='audio/mpeg' <source src='songs/deadshot.mp3'></audio>
          <audio id='double_tap'>         type='audio/mpeg' <source src='songs/double_tap.mp3'></audio>
          <audio id='phd_flooper'>        type='audio/mpeg' <source src='songs/phd_flooper.mp3'></audio>
          <audio id='juggernaut'>         type='audio/mpeg' <source src='songs/juggernaut.mp3'></audio>
          <audio id='mule_kick'>          type='audio/mpeg' <source src='songs/mule_kick.mp3'></audio>
          <audio id='quick_revive'>       type='audio/mpeg' <source src='songs/quick_revive.mp3'></audio>
          <audio id='sleight_of_hand'>    type='audio/mpeg' <source src='songs/sleight_of_hand.mp3'></audio>
          <audio id='stamin_up'>          type='audio/mpeg' <source src='songs/stamin_up.mp3'></audio>
          <audio id='whos_who'>           type='audio/mpeg' <source src='songs/whos_who.mp3'></audio>
          <audio id='tombstone'>          type='audio/mpeg' <source src='songs/tombstone.mp3'></audio>
          <audio id='vulture_aid'>        type='audio/mpeg' <source src='songs/vulture_aid.mp3'></audio>
          <audio id='electric_cherry'>    type='audio/mpeg' <source src='songs/electric_cherry.mp3'></audio>
          <audio id='pack_a_punch'>       type='audio/mpeg' <source src='songs/pack_a_punch.mp3'></audio>
        </form>
    </body>
</html>
"
