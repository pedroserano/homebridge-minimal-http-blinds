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

#### 1] Install it into your homebridge instance

The installation instructions differ depending on how you installed homebridge. Until a more elegant program is written using noble or some other program that directly connects homebridge with the blinds, this solution requires a python script to both interface with the blinds (one at a time) and an httpserver for the urls to call in the homebridge plugin. This is super ugly and hacked together, but for now it works.

Usually this will install it:
````bash
sudo apt install -y python3-pip
pip3 install pygatt
pip3 install pexpect
sudo npm install -g homebridge-mysmartblinds
````
Finally, copy the two python files, httpserver.py and pysmartblinds.py to your raspberry pi's home folder.

#### 2] Minimal configuration

Here is a homebridge `config.json` with the minimal valid configuration. The bridge information is already there unless you have not set up homebridge yet. You must add an accessory for each blind, and create a name for each blind, and change the ip address to wherever you are running the python script, this assumes you are running it on the same device as your homebridge. Also change the "living_room" to whatever you named the blind in httpserver.py:

````json
{
    "bridge": {
        "name": "DemoMinimalisticHttpBlinds",
        "username": "AA:BB:CC:DD:EE:FF",
        "port": 51826,
        "pin": "123-45-678"
    },
  
    "description": "DEV NODEJS MACBOOK",
  
    "accessories": [
        {
    "accessory": "mysmartblinds",
	"name": "Living Room",
  
    "get_current_position_url": "http://127.0.0.1:1500/living_room/pos",
    "set_target_position_url": "http://127.0.0.1:1500/living_room/set/%position%",
    "get_current_state_url": "http://127.0.0.1:1500/living_room/pos",
        }
  
    ],
  
    "platforms": []
}
````

Beware, these three parameters are not checked!  
(`get_current_position_url`, `set_target_position_url`, `get_current_state_url`)  
If you forgot to write them in your accessory, the module will crash.

Also, in the `set_target_position_url` parameter, the placeholder `%position%` will be replaced by the value selected in the iPhone's Home App. 


________________________________________

[Click here](EXAMPLE.MD) to see an example implementation of this HTTP server.

#### 3] Configuration to run the httpserver.py at startup using systemd (just like the instructions for having homebridge running using systemd)

`sudo nano /lib/systemd/system/pysmartblinds.service

Add the following text:
```
[Unit]
Description=My Script Service
After=multi-user.target

[Service]
WorkingDirectory=/home/pi/
User=pi
Type=idle
ExecStart=/usr/bin/python3 /home/pi/httpserver.py
Restart=always

[Install]
WantedBy=multi-user.target
```
exit by hitting ctrl-x and hitting y to save.
Then continue with the following commands to start it up:
```
sudo chmod 644 /lib/systemd/system/pysmartblinds.service
sudo systemctl daemon-reload
sudo systemctl enable pysmartblinds.service
sudo systemctl start pysmartblinds.service
```
And if you want to check the status:

`sudo systemctl status pysmartblinds.service`

The httpserver.py should now be running.

# That's all

## Enjoy
