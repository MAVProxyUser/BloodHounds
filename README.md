Project BloodHounds, autonomous pack hunting armed robotic quadrupeds in a prepackaged "game"

Looking for Quadruped friends? Join "The Dog Pound animal control for Stray robot dogs" slack group: 
https://join.slack.com/t/robotdogs/shared_invite/zt-1fvixx89u-7T79~VxmDYdFSIoTnSagFQ

* [Gelblaster Sentry!](#gelblaster-sentry)
* [Project Bloodhound](#project-bloodhound)
   * [How it Started](#how-it-started)
   * [How it's Going](#how-its-going)
* [Gamification of existing hardware](#gamification-of-existing-hardware)
* [Needs](#needs)
* [Implementation](#implementation)
* [Dogs of War](#dogs-of-war)
* [Setting the final stage](#setting-the-final-stage)
* [Morality of it all?](#morality-of-it-all)

![Dog with gun](https://github.com/MAVProxyUser/BloodHounds/blob/main/dog_with_gun.png)

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

Lots of progress has been made on the GelBlaster turret aka Wingman. The goal is to eventually get it moved onto a robot dog's back as a payload. You can follow along the project specifics here: https://github.com/MAVProxyUser/Gelblaster_Wingman <br>

# Project Bloodhound
Autonomous packhunting robot quadrupeds with Gelblaster Wingman payload coordinated to hande a task such as "protect this object", "patrol this perimeter", "swarm the point of interest". The optional use of the Wingman payload allows for more *serious* blocks of logic to be developed around personal defense. The wingman payload could for example be swapped out for .68 calibre pepper mace paintballs, a standard in self / home Defense products. 

## How it Started
Some of this concept was spitballed on Twitter:<br>

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

## How it's Going
A few of us continued hammering away at the idea after the initial tweets. We are currently looking at the realities of achieving gamification of the existing robot quadruped landscape. 

- What are the limitations (battery life, terrain, potential blaster tech requirements, our ROS ability, access to dogs to dev with)
- Soliciting feedback (including potential features) from folks that would want to play a game like this, or help architect one. 
- Active prototyping of the turret payload aka Wingman. https://github.com/MAVProxyUser/Gelblaster_Wingman
- Active prototyping of targeting vision systems using RasPi, and NVidia Jetson platforms with OpenCV
- Active prototyping of sensors for a fused targeting model: FLIR Lepton, Intel RealSense D435i, D455i, RasPI HD Cam + Lens options, ArduCam 16MP

# Gamification of existing hardware
It makes most sense to use the available commodity hardware for now. Nothing overly custom should be needed. 
- Unitree dogs as the main support base: Several team members have the go1 platform
- Gelblaster Surge XL custom payload aka [Wingman](https://github.com/MAVProxyUser/Gelblaster_Wingman) use for targeting players autonomously, or remotely by other players 
- Gelblaster "surprise box", explosion simulator. Think confetti cannon that throws Gellets everywhere. Can be used for "plant the bomb", or "VIP" style games where the dog with the "surprise box" is denoted as the VIP for one team to protect, and the other team to capture.  

# Needs
Several steps forward have been taken, [several more](https://github.com/users/MAVProxyUser/projects/1) need to be taken just the same.

- ROS Mapping with ability to send dogs to point on map to engage human players (preferably using the NAV2 stack)
- Start on ROS examples to coordinate getting dogs to a specific location. 
- Start on generic *hunting* code and dog2dog comms
- Design a gimbal for Wingman payload!!!! (Dynamixel MX28 looks like a promising platform)
- Work on a hit registration hardware target package that players can hit to disable the dog after so much health is gone
- Target associated health meter that looks like Zelda hearts depleting
- Scoring system
- More dogs for our team to test with. We need a sugar daddy to buy us more robo dogs. 
- Mo money, mo people! https://www.youtube.com/watch?v=c7AL44keDZw


# Implementation
The following packages may be useful in the final implementation logic to enable the dogs to both hunt, and swarm targets
- Swarming - http://wiki.ros.org/micros_swarm_framework
- Wavefront Frontier Detection - https://github.com/SeanReg/nav2_wavefront_frontier_exploration
- Mexplore2 - https://github.com/robo-friends/m-explore-ros2.git
- Dynamixel SDK - https://github.com/ROBOTIS-GIT/DynamixelSDK

# Dogs of War
The sad reality is that dogs have always been used to hunt men. One terrifying account that resonates with me personally is from "The Black phalanx; a history of the Negro soldiers of the United States in the wars of 1775-1812, 1861-'65"

![The Black Phalanx](https://github.com/MAVProxyUser/BloodHounds/blob/main/BlackPhalanx.jpg)
https://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=ha102744390

"Bloodhounds were universally used throughout the South to capture runaway slaves, & were specifically bred for that purpose...  one can imagine the reaction... when they finally got the chance to fight back against this vicious symbol of their oppression"<br> 
http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0021%3Achapter%3D10

![Terrible Fight with Bloodhounds](https://github.com/MAVProxyUser/BloodHounds/blob/main/TerribleFightWithBloodhounds.png)

I'd admittedly not read the specific historical account before seeing the imagery, however after I read up my initial reaction was 'screw that dog'! Having the desire to fight a dog was never something I had in me. Now all the sudden, I think I'm ready. It seems some of my peers are too. 

This image needs updated, but yes, YES, I feel it now, we DO wanna fight robot dogs!! Lets gooooo! 
![Screw that dog](https://github.com/MAVProxyUser/BloodHounds/blob/main/ScrewThatDog.png)

# Setting the final stage
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

# Morality of it all? 
Oh, you wanna talk morals all the sudden, well buckle up. We need to talk about ROSM, RTK, WMI, GVSC, Weaponization & Boston Dynamics Open letter...
https://discourse.ros.org/t/we-need-to-talk-about-rosm-rtk-wmi-gvsc-weaponization-boston-dynamics-open-letter/28235
