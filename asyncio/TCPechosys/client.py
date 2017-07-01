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

async def tcp_echo_client(msg,loop):
    reader, writer = await asyncio.open_connection(host,port,loop=loop)

    print("Send: %r" % msg)
    writer.write(msg.encode())

    data = await reader.read(100)
    print("Received: %r" % data.decode())

    print("Close The Socket")
    writer.close()


loop = asyncio.get_event_loop()

loop.run_until_complete(tcp_echo_client(msg,loop))
loop.close()
