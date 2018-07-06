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

[Click here](EXAMPLE.MD) for step-by-step instructions.

# Enhancements I would love help with

- Using noble to communicate directly between homebridge and the ble blinds, which would probably help with connection and timeout issues
- Finding the ble code for battery status, and adding a homebridge characteristic to support reporting on battery level in homekit
- Support for 0 to 200 down closed to up closed on the blinds, not just 0 to 100 down closed to open, to support tilting closed all the way up and down
