# Real Perk-A-Cola Bottles

[Perk-A-Cola](http://callofduty.wikia.com/wiki/Perk-a-Cola) are a feature that
can be found in zombies maps of Call Of Duty game. Each drink gives the player
a perk to help them survive and fend off the zombie hordes.

More info about this project: [Real Perk-A-Cola Bottles](http://felipeng.net/blog/projetos/real-perk-a-cola-bottles)

## About

This is my own version of Perk-A-Cola in real world with a plus, you can turn
on/off the bottle and play/stop the Perk-A-Cola song through the web interface
which communicate with the GPIO pins of the RaspBerry Pi.

The main file is index.cgi which contains: HTML5 + CSS + JavaScript + GPIO commands

The same code can be modified and used to communicate with microcontrollers,
like [Arduino](http://www.arduino.cc)

## Installation

You have to install:

1. bash
2. [wiringPi](http://wiringpi.com)
3. Any HTTP server with CGI module

### Wiring

It's very simple, the cathode of all LEDs goes to the GND and anode to the
respective pin number.

After that you need to configure the file "pinmap.conf" it's a relationship between
perk and pins

Note: the script use the physical pins of RaspBerry Pi not the GPIO number.

# License

See LICENSE file

# Author

Felipe Nogaroto Gonzalez - < felipeng84 @ gmail . com >
