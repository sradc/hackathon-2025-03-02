import asyncio

from retreival.main import run_search_and_extract


async def main():
    results = await run_search_and_extract("1 bed flat in south London, £1-2k pcm")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
