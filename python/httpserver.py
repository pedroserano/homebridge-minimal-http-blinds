#!/usr/bin/env python3
""" Provides a webserver with push/get endpoints for controlling blinds. """

# pylint: disable=import-error,invalid-name

from http.server import HTTPServer, BaseHTTPRequestHandler
from pysmartblinds import Blind

SERVER_ADDRESS = ('', 1500)

BLINDS = {
    'living_room': {
        'description': 'Living Room Left',
        'mac': 'FA:0E:CD:8D:5E:86',
        'key': (0x40, 0x08, 0x4a, 0x9a, 0x44, 0x74, 0xff)
    },
}

def init_devices():
    """ Configures devices and puts them into known states. """
    for blind in BLINDS:
        blind = BLINDS[blind]
        blind['blind'] = Blind(blind['mac'], blind['key'])
        blind['blind'].pos(0)


class HTTPHandler(BaseHTTPRequestHandler):
    """ Handles HTTP events """
    def do_POST(self):
        """ Handles POST requests """
        params = self.path.split('/')
        # Parse and check command
        if len(params) < 3:
            self.send_error(404)
            return
        blind, action = params[1:3]
        params = params[3:]

        # Parse and check command
        if blind not in BLINDS or action not in ('up', 'down', 'stop', 'set'):
            self.send_error(404)
            return
        if action == 'set' and (len(params) == 0 or not params[0].isdigit()):
            self.send_error(404)
            return

        # Get the device to control
        blind = BLINDS[blind]['blind']
        # Send the command
        response = 500
        try:
            if action == 'up':
                response = blind.up()
            elif action == 'down':
                response = blind.down()
            elif action == 'stop':	
                response = blind.stop()
            elif action == 'set':
                response = blind.pos(params[0], len(params) >= 2 and params[1])
            response = response and 204 or 504
        except Blind.BLEError as exception:
            self.send_response(500)
            self.end_headers()
            raise exception

        # Reply to the request
        self.send_response(response)
        self.end_headers()

    def do_GET(self):
        """ Handles GET requests """
        params = self.path.split('/')
        if len(params) != 3:
            self.send_error(404)
            return

        # Parse and check command
        _, blind, action = params
        if action != 'pos' or blind not in BLINDS:
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = str(BLINDS[blind]['blind'].pos())
        self.wfile.write(message.encode('utf-8'))


if __name__ == "__main__":
    init_devices()
    HTTPServer(SERVER_ADDRESS, HTTPHandler).serve_forever()
