#!/usr/bin/env python3
"""
Membit Python SDK - Example

Set your MEMBIT_API_KEY environment variable:
    export MEMBIT_API_KEY="your_api_key_here"
    uv sync
    uv run examples/client.py
"""

from membit import MembitClient


def main():
    # Initialize client
    client = MembitClient()

    # Search for trending clusters
    print("Searching for trending clusters... ")
    clusters = client.route_cluster_search(q="artificial intelligence", limit=3)
    print("Clusters:", clusters)

    print("--------------------------------")

    # Get cluster info
    print("Getting cluster info... ", clusters["clusters"][0]["label"])
    cluster_info = client.route_cluster_info(
        label=clusters["clusters"][0]["label"], limit=3
    )
    print("Cluster info:", cluster_info)

    print("--------------------------------")

    # Search for posts
    print("Searching for posts... ")
    posts = client.post_search(q="artificial intelligence", limit=3)
    print("Posts:", posts)


if __name__ == "__main__":
    main()
