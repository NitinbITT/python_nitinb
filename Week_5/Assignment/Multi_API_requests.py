"""Question 3: Async API Client with Retries & Timeouts

Build an async application that fetches data from multiple APIs concurrently:
Use aiohttp or httpx to make async HTTP requests
Fetch data from your api's
Implement:
Timeout handling (2 seconds per request)
Retry logic (max 3 retries with exponential backoff)
Graceful error handling for failed requests
Concurrent execution of all requests using asyncio.gather() or asyncio.create_task()

Display results showing which requests succeeded/failed
Show total execution time vs sequential time"""

import asyncio
import httpx
import time

URLS = [
    "http://localhost:8000/books",
    "http://localhost:8000/books/1",
    "http://localhost:8000/books/100",
]


async def fetch_with_retry(client, url):
    retries = 3
    delay = 1

    for attempt in range(retries):
        try:
            response = await client.get(url, timeout=2.0)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            if attempt < retries - 1:
                await asyncio.sleep(delay)
                delay *= 2
            else:
                return "error" + str(e)


async def run_concurrent():
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in URLS:
            tasks.append(fetch_with_retry(client, url))

        results = await asyncio.gather(*tasks)
        return results


async def run_sequential():
    results = []
    async with httpx.AsyncClient() as client:
        for url in URLS:
            result = await fetch_with_retry(client, url)
            results.append(result)
    return results


async def main():

    print("Running Concurrent Requests")
    start = time.perf_counter()
    concurrent_results = await run_concurrent()
    concurrent_time = time.perf_counter() - start

    for result in concurrent_results:
        print(result)

    print("Concurrent Time:", concurrent_time)

    print("\nRunning Sequential Requests")
    start = time.perf_counter()
    sequential_results = await run_sequential()
    sequential_time = time.perf_counter() - start

    for result in sequential_results:
        print(result)

    print("Sequential Time:", sequential_time)


if __name__ == "__main__":
    asyncio.run(main())
