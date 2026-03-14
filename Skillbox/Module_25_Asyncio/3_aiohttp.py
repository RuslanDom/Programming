import asyncio
import aiohttp
import aiofiles
from pathlib import Path

URL = "https://cataas.com/cat"
CATS_WE_WANT = 5
OUT_PATH = (Path(__file__).parent/ 'cats').absolute()



async def get_cat(client: aiohttp.ClientSession, id: int):
    async with client.get(URL) as response:
        print(response.status)
        cat = await response.read()
        await write_cats(pic=cat, id=id)


async def write_cats(pic: bytes, id: int):
    file_path = "{}/{}.png".format(OUT_PATH, id)
    async with aiofiles.open(file_path, 'wb') as file:
        await file.write(pic)


async def get_all_cats():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10)) as session:
        tasks = [get_cat(session, inx) for inx in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)

def main():
    result = asyncio.run(get_all_cats())
    print(len(result))

if __name__ == '__main__':
    main()
