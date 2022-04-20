import aiohttp
import asyncio
import pprint


URL = 'https://swapi.dev/api/people/'


async def main(url):
    async with aiohttp.ClientSession() as session:
        people = []
        NUM = 1
        while True:
            async with session.get(url+f'?page={NUM}', ssl=False) as resp:
                text = await resp.json()
                results = text['results']
                # pprint.pprint(results)
                people += results
                if text['next'] == None:
                    break
                NUM += 1
        return people

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
personages = asyncio.run(main(URL))

async def get_string_films(films):
    for film in films:
        async def get_film(film):
            async with aiohttp.ClientSession() as session:
                pass


if __name__ == '__main__':

    # pprint.pprint(len(personages))
    print(personages[0]['films'])
