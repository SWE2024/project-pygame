import asyncio
import sys
from ip import port, ip
from concurrent.futures import ThreadPoolExecutor



async def ainput() -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input)

async def send_data(writer, name):
    while True:
        try:
            message = await ainput()
            message = name + "|" + message
            data = message.encode()
            data += b' ' * (1024 - len(data))
            writer.write(data)
            await writer.drain()
            await asyncio.sleep(1/12)
            # print("drained properly")
        except KeyboardInterrupt as err:
            writer.write("!disconnect".encode())
            await writer.drain()
            print("chat closed")
            return

async def receive_data(reader):
    count = 0
    while True:
        # print(f"receive_data {count}")
        try:
            data = await reader.read(1024)
            name, message = data.decode().split('|')
            print(f"{name}:\t", message.rstrip())
        except KeyboardInterrupt as err:
            return
        
        count += 1

async def main(name):
    print(f'joining chat at {ip}:{port}')
    reader, writer = await asyncio.open_connection(ip, port)

    send_task = asyncio.create_task(send_data(writer, name))
    receive_task = asyncio.create_task(receive_data(reader))

    await asyncio.gather(send_task, receive_task)

    # try:
    #     await asyncio.wait([send_task, receive_task], timeout=3600)
    # finally:
    #     send_task.cancel()

if __name__ == "__main__":
    # name = input('Enter your name:\t')
    name = "jesus"
    asyncio.run(main(name))