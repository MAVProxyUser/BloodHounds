* [Gelblaster Sentry!](#gelblaster-sentry)
* [Project Bloodhound](#project-bloodhound)
   * [How it Started](#how-it-started)
   * [How it's Going](#how-its-going)
* [Setting the Stage](#setting-the-stage)
* [Dogs of War](#dogs-of-war)
* [Implementation](#implementation)

![Dog with gun](https://github.com/MAVProxyUser/BloodHounds/blob/main/dog_with_gun.png)

Looking for Quadruped friends? Join "The Dog Pound animal control for Stray robot dogs" slack group: 
https://join.slack.com/t/robotdogs/shared_invite/zt-1fvixx89u-7T79~VxmDYdFSIoTnSagFQ

# Gelblaster Sentry!
**~~Paintball Sentry?~~**
For years I've wanted to create a paintball sentry turret. My family has sold paintball guns for 2 decades now, so this has been a persistent thought in my head. https://realsentrygun.com. Now we sell Gelblasters at our store, so my brain has wandered a bit... 

One of the first examples I can remember is a briefcase based version. 
[![briefcase sentry](http://img.youtube.com/vi/mP6LgxkhMzY/0.jpg)](https://www.youtube.com/watch?v=mP6LgxkhMzY)<br>

There was eventually a viral video to go along with the implementation. 
[![viral sentry](http://img.youtube.com/vi/6QcfZGDvHU8/0.jpg)](https://www.youtube.com/watch?v=6QcfZGDvHU8)<br>

12 years later I finally one upped the idea I had in my head, although admiditedly not automated, *yet*. 
https://twitter.com/d0tslash/status/1561205492499845122
[![Gelblaster Robodog vs neighbor](http://img.youtube.com/vi/7_qtMKeWV4M/0.jpg)](https://www.youtube.com/watch?v=7_qtMKeWV4M)<br>

# Project Bloodhound

## How it Started
"I’m trying to figure out what people would pay for me to come and do with the dog or pay to rent to do."
...
"TLDR: consensus was Sex maids"<br>
https://twitter.com/AndrewKemendo/status/1569162469465104387

"Of course folks out here like..."<br>
https://twitter.com/d0tslash/status/1569175110363267072

"I'm thinking like a paint ball field, with multiple non-lethal armed dogs, & your task is to not get eliminated by them. Give em some sort of 
target to disable the dog to be fair. Play classic red vs blue elimination & payload delivery games. Swap turns as dog operators & hunted."<br>
https://twitter.com/d0tslash/status/1569179857694629888

"I would quit my day job to make this"<br>
https://twitter.com/DustinHLand/status/1569211528259448832

## How it's Going
Currently looking at the realities of acheiving gamification of the existing robot quadruped landscape. 
- What are the limitations (battery life, terrain, potential blaster tech requirements, our ROS ability, access to dogs to dev with)
- Soliciting feedback (including potential features) from folks that would want to play a game like this, or help architect one. 

"Being stalked around Caesars by half a dozen, remotely operated robot dog assassins 🤔 your one job is to gain entry, obtain the loot, and exfil all without being shot by the gel blaster 😅 love it"<br>
https://twitter.com/Clarkee/status/1569325186713006085

"Humans should have some low level EW stuff too, like a scanner that is useful but also anxiety inducing :D"<br>
https://twitter.com/Clarkee/status/1569399751074025472

"Blue light mode = undetected
Red light mode = detected
Yellow = searching"<br>
https://twitter.com/DustinHLand/status/1569399657767247873

"We could lidar map the arena and use a ros node to coordinate a swarm so they converge on a target."<br>
https://twitter.com/DustinHLand/status/1569399657767247873

# Setting the Stage
The dystopian future nobody wanted, or asked for is already on the way. Why not train for it, everyone else is!? At least we can have a little fun in the process. 

"Robot dogs join US Air Force exercise giving glimpse at potential battlefield of the future"<br>
electronic canines are just one link in what the US military calls the Advanced Battle Management System (ABMS)... We are exploring how to use ... ABMS to link sensors to shooters across all battlespaces, at speed and under threat. Maturing these concepts and capabilities is necessary to fight and win in the information age<br>
https://www.cnn.com/2020/09/09/us/robot-dogs-us-air-force-test-intl-hnk-scli-scn/index.html

"Robot Dogs Take Another Step Towards Deployment at the Border"<br>
The goal of the program is to leverage technology to force-multiply the CBP presence... So, don’t be surprised if in the future we see robot “Fido” out in the field, walking side-by-side with CBP personnel.<br>
https://www.dhs.gov/science-and-technology/news/2022/02/01/feature-article-robot-dogs-take-another-step-towards-deployment

"N.Y.P.D. Robot Dog’s Run Is Cut Short After Fierce Backlash"<br>
The Police Department will return the device earlier than planned after critics seized on it as a dystopian example of overly aggressive policing.<br>
https://www.nytimes.com/2021/04/28/nyregion/nypd-robot-dog-backlash.html

"Honolulu Police Used a Robot Dog to Patrol a Homeless Encampment"<br>
Despite widespread public outrage at police departments’ use of Boston Dynamics' Spot robot, law enforcement agencies continue to look for ways to experiment with the headless, quadrupedal machine.<br>
https://www.vice.com/en/article/wx5xym/honolulu-police-used-a-robot-dog-to-patrol-a-homeless-encampment

I'll spare you the now cliche "Robot dog with gun", or "Robot dog with Rocket Launcher" prototype stories. That is of course part of why you are here, you already know what's up.

# Dogs of War
The sad reality is that dogs have always been used to hunt men. One terrifying account that resonates with me personally is from "The Black phalanx; a history of the Negro soldiers of the United States in the wars of 1775-1812, 1861-'65"

![The Black Phalanx](https://github.com/MAVProxyUser/BloodHounds/blob/main/BlackPhalanx.jpg)
https://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=ha102744390

"Bloodhounds were universally used throughout the South to capture runaway slaves, & were specifically bred for that purpose...  one can imagine the reaction... when they finally got the chance to fight back against this vicious symbol of their oppression"<br> 
http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0021%3Achapter%3D10

![Terrible Fight with Bloodhounds](https://github.com/MAVProxyUser/BloodHounds/blob/main/TerribleFightWithBloodhounds.png)

I'd admittedly not read the specific historical account before seeing the imagery, however after I read up my initial reaction was 'screw that dog'! Having the desire to 
fight a dog was never something I had in me. Now all the sudden, I think I'm ready. It seems some of my peers are too. 

This image needs updated, but yes, YES, I feel it now, we DO wanna fight robot dogs!! Lets gooooo! 
![Screw that dog](https://github.com/MAVProxyUser/BloodHounds/blob/main/ScrewThatDog.png)

# Gamification of existing hardware

- Unitree Go1, or Xiaomi yberdog support base
- Gellblaster Surge Payload
- Gellblaster "surprise box", explosion simulator. Think confetti cannon that throws gelets everywhere. 
- Hit registration package(?) for the dog to temporarily disable
- Scoring system
- ROS Mapping with ability to send dogs to point on map to engage human players

# Needs
- More dogs
- Gelblaster Surge with no handle, and more easily accessible electronics
- Gimbal!!!!
- Start on ROS examples to coordinate getting dogs to a specific location. 
- Start on generic *hunt* code and dog2dog comms
- Work on a target that players can hit to disable the dog
- Mo money, mo people! 

# Implementation
- Swarming - http://wiki.ros.org/micros_swarm_framework
