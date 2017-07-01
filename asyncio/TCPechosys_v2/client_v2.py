#!/usr/bin/env python3

#_____________________________________________________________________________
#
# A simple TCP echo client with asynchio
#
# Author:   Samdney  <contact@carolin-zoebelein.de>
#           D4A7 35E8 D47F 801F 2CF6 2BA7 927A FD3C DE47 E13B 
# License:  See LICENSE for licensing information
#_____________________________________________________________________________

# Code after tutorial on: https://asyncio.readthedocs.io/en/latest/tcp_echo.html


import asyncio

host = "127.0.0.1"
port = 8888

msg = "Hallo"


class Client():

    def __init__(self):
        self.reader = None
        self.writer = None
        self.host = host
        self.port = port

    async def connect(self,loop):
        self.reader, self.writer = await asyncio.open_connection(self.host,self.port,loop=loop)

    def write(self,msg):
        print("Send: %r" % msg)
        self.writer.write(msg.encode())

    async def read(self,msg):
        data = await self.reader.read(100)
        print("Received: %r" % data.decode())

    def close(self):
        print("Close The Socket")
        self.writer.close()


async def tcp_echo_client(mgs,loop):

    print("TCP echo client")
    myClient = Client()
    await myClient.connect(loop)
    myClient.write(msg)
    await myClient.read(msg)
    myClient.close()


# entry point
loop = asyncio.get_event_loop()

loop.run_until_complete(tcp_echo_client(msg,loop))
loop.close()
