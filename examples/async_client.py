#!/usr/bin/env python3
"""
Membit Python SDK - Asynchronous Example

Set your MEMBIT_API_KEY environment variable:
    export MEMBIT_API_KEY="your_api_key_here"
    uv sync
    uv run examples/async_client.py
"""

from membit import AsyncMembitClient


async def main():
    # Initialize client
    client = AsyncMembitClient()

    # Search for trending clusters
    print("Searching for trending clusters... ")
    clusters = await client.route_cluster_search(q="artificial intelligence", limit=3)
    print("Clusters: ", clusters)

    print("--------------------------------")

    # Get cluster info
    print("Getting cluster info... ", clusters["clusters"][0]["label"])
    cluster_info = await client.route_cluster_info(
        label=clusters["clusters"][0]["label"], limit=3
    )
    print("Cluster info: ", cluster_info)

    print("--------------------------------")

    # Search for posts
    print("Searching for posts... ")
    posts = await client.post_search(q="artificial intelligence", limit=3)
    print("Posts: ", posts)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
