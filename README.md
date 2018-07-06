# homebridge-mysmartblinds

### What is it?

**homebridge-mysmartblinds** is a minimalistic mysmartblinds management plugin for homebridge using python.

The features:
- You can control your own mysmartblinds.
- The control is not a simple binary open/close: **it support percentages**. You can open your blinds at 50% or 65% for instance.
- Your blinds can still be otherwise operated by the onboard schedule, hub, or mysmartblinds app.

### Who is it for?

Anyone who, just like me, doesn't know much about homebridge
but still wants a straightforward way to communicate with your mysmartblinds (hopefully until they release native homekit compatibility. PLEASE!).

### How to use it

#### 1] Install the python server for interfacing with your mysmartblinds

````bash
sudo apt install -y python3-pip
pip3 install pygatt
pip3 install pexpect
````
Finally, copy the two python files, httpserver.py and pysmartblinds.py to your raspberry pi's home folder.
You must either run the program from the command line by typing:
`python3 httpserver.py` 
or setting up a systemd process to run it automatically as per the directions below.

#### 2] Install it into your homebridge instance

The installation instructions differ depending on how you installed homebridge. Until a more elegant program is written using noble or some other program that directly connects homebridge with the blinds, this solution requires a python script to both interface with the blinds (one at a time) and an httpserver for the urls to call in the homebridge plugin. This is super ugly and hacked together, but for now it works.

Usually this will install it:
````bash
sudo npm install -g homebridge-mysmartblinds
````

________________________________________

[Click here](EXAMPLE.MD) for step-by-step instructions.

# Enjoy
