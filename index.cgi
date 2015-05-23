#!/bin/bash

# Real Perk-A-Cola Bottles LED
# Created by Felipe Nogaroto Gonzalez
# License: MIT

# Verificar se o comando gpio existe

no_gpio(){
  echo -e "Content-Type: text/html\r\n

  <html>
    <head>
    </head>
    <body>
      gpio not found
    </body>
  </html>
  "
  exit
}

GPIO=$(which echasdao || echo o no_gpio)
exit

# Inicializa todos os pinos como OUT e como 0
for pin in $(seq 0 12); do
  echo gpio mode $pin out
  echo gpio write $pin 0
done



echo -e 'Content-Type: text/html\r\n'

# Parser pin and value
PIN='${QUERY_STRING/=*}'
VALUE='${QUERY_STRING/*=}'

if [ $VALUE == 0 -o $VALUE == 1 ]; then
  echo 'gpio write $PIN $VALUE' >> /tmp/teste.log
  #gpio write $PIN $VALUE
fi

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
    	   var music = document.getElementById('music-' + perk.id);
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
    	    <img class='perk gray' onclick='player(this);' id='1'  src='imgs/deadshot.png'        alt='Deadshot Daiquiri'>
    	    <img class='perk gray' onclick='player(this);' id='15' src='imgs/double_tap.png'      alt='Double Tap Root Beer'>
    	    <img class='perk gray' onclick='player(this);' id='11' src='imgs/phd_flooper.png'     alt='PhD Flooper'>
    	    <img class='perk gray' onclick='player(this);' id='10' src='imgs/juggernaut.png'      alt='Juggernaut'>
    	    <img class='perk gray' onclick='player(this);' id='6'  src='imgs/mule_kick.png'       alt='Mule Kick'>
    	    <img class='perk gray' onclick='player(this);' id='16' src='imgs/quick_revive.png'    alt='Quick Revive'>
	        <img class='perk gray' onclick='player(this);' id='5'  src='imgs/sleight_of_hand.png' alt='Sleight Of Hand'>
	        <img class='perk gray' onclick='player(this);' id='4'  src='imgs/stamin_up.png'       alt='Stamin-Up'>
	        <img class='perk gray' onclick='player(this);' id='9'  src='imgs/whos_who.png'        alt='Whos Who'>
	        <img class='perk gray' onclick='player(this);' id='10' src='imgs/tombstone.png'       alt='Tombstone'>
	        <img class='perk gray' onclick='player(this);' id='11' src='imgs/vulture_aid.png'     alt='Vulture Aid Elixir'>
	        <img class='perk gray' onclick='player(this);' id='12' src='imgs/electric_cherry.png' alt='Electric Cherry'>
	        <img class='perk gray' onclick='player(this);' id='99' src='imgs/pack_a_punch.png'    alt='Pack A Punch'>
          <audio id='music-0'>  type='audio/mpeg' <source src='songs/deadshot.mp3'></audio>
          <audio id='music-1'> type='audio/mpeg' <source src='songs/double_tap.mp3'></audio>
          <audio id='music-2'> type='audio/mpeg' <source src='songs/phd_flooper.mp3'></audio>
          <audio id='music-3'> type='audio/mpeg' <source src='songs/juggernaut.mp3'></audio>
          <audio id='music-4'>  type='audio/mpeg' <source src='songs/mule_kick.mp3'></audio>
	        <audio id='music-5'> type='audio/mpeg' <source src='songs/quick_revive.mp3'></audio>
	        <audio id='music-6'>  type='audio/mpeg' <source src='songs/sleight_of_hand.mp3'></audio>
	        <audio id='music-7'>  type='audio/mpeg' <source src='songs/stamin_up.mp3'></audio>
	        <audio id='music-8'>  type='audio/mpeg' <source src='songs/whos_who.mp3'></audio>
  	      <audio id='music-9'> type='audio/mpeg' <source src='songs/tombstone.mp3'></audio>
  	      <audio id='music-10'> type='audio/mpeg' <source src='songs/vulture_aid.mp3'></audio>
	        <audio id='music-11'> type='audio/mpeg' <source src='songs/electric_cherry.mp3'></audio>
	        <audio id='music-99'> type='audio/mpeg' <source src='songs/pack_a_punch.mp3'></audio>
        </form>
    </body>
</html>
"
