forked from https://github.com/RyanteckLTD/RTK-000-003/blob/master/handyTipsGuides/powerMethods.md

##USB Battery Bank / Emergency Phone Bank
####Between £10-15 for a normal one, £20+ for extra capacity. Recommended

This is the easiest method of powering your Raspberry Pi as it plug and play. They normally take 5-10 hours to charge up depending on the charge level and the size of the bank.

I use the one from CPC on my robots and they can last from 2.5-4 hours depending on what work the Pi is doing (with even longer on a Model A).

***Recommended places to buy:***

CPC (UK & IE) - http://cpc.farnell.com/jsp/search/productdetail.jsp?SKU=BT05752 , Tried & Tested - 2.5-4 hours depending on usage and charge level.

Adafruit (US) - http://www.adafruit.com/products/1565 , Not tried & Tested yet. Estimated 3-5 Hours. (Also available in double capacity http://www.adafruit.com/products/1566)

RS Electronics (UK) - http://uk.rs-online.com/web/p/power-banks/7757504/ , Not Tried & Tested but recommended by other Raspberry Pi'ers online. (Also double capacity at http://uk.rs-online.com/web/p/power-banks/7757508/)

##DC to DC Regulators
#### Between £2-6 
A DC to DC regulator is an more advanced Voltage Regulator allowing you to set the output voltage and is also more efficient from where it does not make the voltage go down by loosing heat but instead by switching it making it also very efficient compared to a normal regulator.

This is an method that we are awaiting to test but we have seen on other projects, you can either use the same power supply as the motors or use another set of batteries (which is recommended). You will either need a Step Up if you are trying to use a voltage lower than 4.5V or a step down if you are using a voltage more than 5.5V

You can find these online on places such as <a href="http://www.amazon.co.uk/s/ref=nb_sb_ss_c_0_8?url=search-alias%3Delectronics&field-keywords=dc%20to%20dc%20converter&sprefix=DC+to+DC%2Caps%2C157" target="_blank">Amazon</a> and <a href="http://www.ebay.co.uk/itm/New-LM2596-DC-Buck-Step-Down-Voltage-Adjustable-Converter-Power-Module-Regulator-/221392566723?pt=UK_BOI_Electrical_Test_Measurement_Equipment_ET&hash=item338c0679c3" target="_blank">Ebay</a> but require calibration to set the voltage using a Multimeter.

Bot Toughts also sell one on <a href="https://www.tindie.com/products/BBTech/tps5430-buck-power-converter-replaceable-78xx-series/" target="_blank">Tindie</a> which we will be trying and testing. (This requires 5.8V to provide 5V so would require ~ 6 AA batteries.

##4 X AA Rechargables
#### ~ £3 to build + battery cost of ~ £10
You are able to get away with 4 AA ***Rechargable*** batteries and plug it directly into the Raspberry Pi. 

***Warning, if you do not use rechargables you have the risk of permantly damaging your Raspberry Pi***

This is from where rechargables produce a voltage of ~ 1.25V each, making it 5V when 4 are used. 

You will need:
* 1 X AA Battery Box (Do not use the same one as the motors due to feedback from the motors)
* 1 X Micro USB Cable to be chopped up
* 1 X Battery Clip - Only required if your battery box is designed to use a PP9 snap on clip. (Warning Do NOT ever plug a 9v battery into this clip).

Build instructions will be written soon.


##Raspberry Pi Battery and UPS Add-ons
There are a couple of systems that may be viable to use for the robot, these are currently being written.

###[MoPi](http://pi.gate.ac.uk/mopi/)
#### >= £24 (£24 for the board + batteries, solar panels, wind turbines, ...)
MoPi is mobile and 24/7 power for the Pi. On your bike, up a tree, or for your
home server:

* multiple inputs: standard batteries, car power sockets, old laptop supplies,
  solar panels, ...
* hot-swap power replacement without stopping work
* shutdown the Pi cleanly when batteries discharge
* integrated on/off switch
* UPS (uninterruptible power) when using both batteries and mains
* on-board LED indicators and on-Pi notifications

###[PiUSV](http://www.piusv.de/)

###[UPS Pico](http://www.modmypi.com/raspberry-pi/breakout-boards/pi-modules/ups-pico)

###[S-USV](http://www.s-usv.de/)
