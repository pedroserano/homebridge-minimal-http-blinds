# Example implementation in Python

## 1] Architecture

- Homebridge server is : `192.168.1.22`
- Raspberry Pi with the Python script controlling the blinds : `192.168.1.55`

## 1] Python Script configuration

Replace the BLINDS section of httpserver.py with your blind information. This requires finding the key. Whatever you name each blind is what needs to go in the config.json urls. The description can be whatever you want, [the MAC address and key you must follow these instructions to get for your own blinds](https://github.com/dnschneid/pysmartblinds/blob/master/README.md).

```
BLINDS = {
'living_room_middle': {
        'description': 'Living Room Middle',
        'mac': 'AA:BB:CC:DD:EE:FF',
        'key': (0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0xaa)
    },
        'living_room_right’: {
        'description': 'Living Room Right’,
        'mac': 'AA:BB:CC:DD:EE:FF',
        'key': (0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0xaa)
    },
        'living_room_left’: {
        'description': 'Living Room Left’,
        'mac': 'AA:BB:CC:DD:EE:FF',
        'key': (0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0xaa)
    },
}
```
## 3] Homebridge accessory configuration

Here is a homebridge `config.json` with the minimal valid configuration. The bridge information is already there unless you have not set up homebridge yet. You must add an accessory for each blind, and create a name for each blind, and change the ip address to wherever you are running the python script, this assumes you are running it on the same device as your homebridge. Also change the "living_room" to whatever you named the blind in httpserver.py: (example with 3, 1 for each blind):

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
        "name": "Living Room Middle",
        "accessory": "mysmartblinds",

    "get_current_position_url": "http://127.0.0.1:1500/living_room_middle/pos",
    "set_target_position_url": "http://127.0.0.1:1500/living_room_middle/set/%position%",
    "get_current_state_url": "http://127.0.0.1:1500/living_room_middle/pos"
    },
    {
        "accessory": "mysmartblinds",
        "name": "Living Room Right",
  
            "get_current_position_url": "http://127.0.0.1:1500/living_room_right/pos",
            "set_target_position_url": "http://127.0.0.1:1500/living_room_right/set/%position%",
            "get_current_state_url": "http://127.0.0.1:1500/living_room_right/pos"
            },
        {
            "accessory": "mysmartblinds",
        "name": "Living Room Left",
  
            "get_current_position_url": "http://127.0.0.1:1500/living_room_left/pos",
            "set_target_position_url": "http://127.0.0.1:1500/living_room_left/set/%position%",
            "get_current_state_url": "http://127.0.0.1:1500/living_room_left/pos"
}

], 
    "platforms": []
}
````

Beware, these three parameters are not checked!  
(`get_current_position_url`, `set_target_position_url`, `get_current_state_url`)  
If you forgot to write them in your accessory, the module will crash.

Also, in the `set_target_position_url` parameter, the placeholder `%position%` will be replaced by the value selected in the iPhone's Home App. 

#### 3] Configuration to run the httpserver.py at startup using systemd (just like the instructions for having homebridge running using systemd)

Enter the following command:
`sudo nano /lib/systemd/system/pysmartblinds.service`

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
