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

async def handle_echo(reader,writer):
    print("Received Client Connection Attempt")

    data = await reader.read(100)
    msg = data.decode()
    addr = writer.get_extra_info("peername")
    print("Received %r from %r" % (msg, addr))

    print("Send: %r" % msg)
    writer.write(data)
    await writer.drain()

    print("Close The Client Socket")
    writer.close()


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

