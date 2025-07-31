#!/usr/bin/env python3
"""
Membit Python SDK - Example

Set your MEMBIT_API_KEY environment variable:
    export MEMBIT_API_KEY="your_api_key_here"
    uv sync
    uv run examples/client.py
"""

from membit import MembitClient


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


def main():
    # Initialize client
    client = MembitClient()
    # or
    # client = MembitClient(api_key="your_api_key_here")

    print_section("Searching for Trending Clusters")
    clusters = client.cluster_search("artificial intelligence", limit=3)
    print("Result:", clusters)

    print_section("Getting Cluster Details")
    label = clusters["clusters"][0]["label"]
    print(f"Fetching details for cluster: {label}")
    cluster_info = client.cluster_info(label, limit=3)
    print("Cluster info:", cluster_info)

    print_section("Searching for Individual Posts")
    posts = client.post_search("artificial intelligence", limit=3)
    print("Posts:", posts)


if __name__ == "__main__":
    main()
