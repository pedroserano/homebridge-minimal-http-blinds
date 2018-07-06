# Example implementation in Python

## 1] Architecture

- Homebridge server is : `192.168.1.22`
- Raspberry Pi with the Python script controlling the blinds : `192.168.1.55`

## 1] Python Script configuration

Replace the BLINDS section of httpserver.py with your blind information. This requires finding the key. Whatever you name each blind is what needs to go in the config.json urls. The description can be whatever you want, the MAC address and key you must follow these instructions to get for your own blinds.

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

Here is the accessory I need to add:

``` json
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

]
```

