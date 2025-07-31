#!/usr/bin/env python3
"""
Membit Python SDK - Asynchronous Example

Set your MEMBIT_API_KEY environment variable:
    export MEMBIT_API_KEY="your_api_key_here"
    uv sync
    uv run examples/async_client.py
"""

from membit import AsyncMembitClient


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


async def main():
    # Initialize client
    client = AsyncMembitClient()
    # or
    # client = AsyncMembitClient(api_key="your_api_key_here")

    print_section("Searching for Trending Clusters (Async)")
    clusters = await client.cluster_search("artificial intelligence", limit=3)
    print("Result:", clusters)

    print_section("Getting Cluster Details (Async)")
    label = clusters["clusters"][0]["label"]
    print(f"Fetching details for cluster: {label}")
    cluster_info = await client.cluster_info(label, limit=3)
    print("Cluster info:", cluster_info)

    print_section("Searching for Individual Posts (Async)")
    posts = await client.post_search("artificial intelligence", limit=3)
    print("Posts:", posts)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
