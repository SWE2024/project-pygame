import asyncio
from ip import port
writer_list = []
ip = 'enter.server.ip.here'

async def send_data(name):
    global writer_list
    try:
        while True:
            message = input("You:\t")
            data = name + "|" + message
            data = data.encode()
            data += b' ' * (1024 - len(data))
            await broadcast(data)

    except KeyboardInterrupt as err:
        print('Closing chat server...')
        message = "!disconnect"
        data = name + "|" + message
        data = data.encode()
        data += b' ' * (1024 - len(data))
        await broadcast(data)

        for writer in writer_list:
            writer.close()

        writer_list = writer

async def handle_client(reader, writer):
    print('new connection made')

    writer_list.append(writer)
    loop = 0
    while True:
        print(loop)
        data = await reader.read(1024)
        name, msg = data.decode().split('|')
        print('message received')
        
        if msg == "!disconnect":
            msg = "Left the chat"
            await broadcast(data, writer)
            writer_list.remove(writer)
            writer.close()
            print(name + ":\t" + msg.rstrip() + "|")
            loop += 1
            continue

        await broadcast(data, writer)
        print(name + ":\t" + msg.rstrip())
        print('message length:', len(msg.rstrip()))
        loop += 1

async def broadcast(message, exclusion = None):
    global writer_list

    print('came into broadcast')
    tasks = []
    for writer in writer_list:
        if writer is exclusion:
            continue
        writer.write(message)
        tasks.append(writer.drain())

    if len(tasks) == 0:
        print('hit here')
        return

    await asyncio.gather(*tasks)

async def main():
    print(f"Starting chat on {ip}:{port}")
    server = await asyncio.start_server(handle_client, ip, port)

    async with server:
        await server.serve_forever()
        await send_data("taisei")
        # await asyncio.gather(server.serve_forever(), send_data("taisei"))


        

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())