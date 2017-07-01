#!/usr/bin/env python3

#_____________________________________________________________________________
#
# A simple TCP echo server with asynchio
#
# Author:   Samdney  <contact@carolin-zoebelein.de>
#           D4A7 35E8 D47F 801F 2CF6 2BA7 927A FD3C DE47 E13B 
# License:  See LICENSE for licensing information
#_____________________________________________________________________________

# Code after tutorial on: https://asyncio.readthedocs.io/en/latest/tcp_echo.html

import asyncio

host = "127.0.0.1"
port = 8888


class Server():
   
    def __init__(self):
        self.msg = ""
        self.data = None

    async def read(self,reader,writer):
        self.data = await reader.read(100)
        self.msg = self.data.decode()
        addr = writer.get_extra_info("peername")
        print("Received %r form %r" % (self.msg,addr))

    async def write(self,writer):
        print("Send: %r" % self.msg)
        writer.write(self.data)
        await writer.drain()

    def close(self,writer):
        print("Close The Client Socket")
        writer.close()

async def  handle_echo(reader,writer):
    print("Received Client Connection Attempt")

    myServer = Server()
    await myServer.read(reader,writer)
    await myServer.write(writer)
    myServer.close(writer)


# entry point
loop = asyncio.get_event_loop()

coro = asyncio.start_server(handle_echo,host,port,loop=loop)
server = loop.run_until_complete(coro)

print("Serving on {}".format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

