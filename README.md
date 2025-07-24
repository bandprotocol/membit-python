# Membit Python Client

[![PyPI - Downloads](https://img.shields.io/pypi/dm/membit-python)](https://pypi.org/project/membit-python/)
[![License](https://img.shields.io/github/license/your-org/membit-python)](https://github.com/your-org/membit-python/blob/main/LICENSE)

The Membit Python client allows for easy interaction with the Membit API, offering powerful social media analytics and monitoring capabilities directly from your Python programs. Easily integrate trending discussion discovery, cluster analysis, and social post search into your applications.

## Installing

```bash
pip install membit-python
```

Or with uv:

```bash
uv add membit-python
```

## Getting Started

To use the Membit API, you'll need an API key. You can set it as an environment variable:

```bash
export MEMBIT_API_KEY="your_api_key_here"
```

Or pass it directly when creating a client instance.

# Trending Discussion Clusters

Find and analyze trending discussions across social platforms with intelligent clustering.

## Usage

Below are some code snippets that show you how to interact with our API. The different steps and components of this code are explained in more detail in the API Methods section further down.

### Finding Trending Discussion Clusters

```python
from membit import MembitClient

# Step 1. Instantiate your MembitClient
client = MembitClient(api_key="your_api_key_here")

# Step 2. Search for trending discussion clusters
clusters = client.route_cluster_search(q="artificial intelligence", limit=5)

# Step 3. That's it! You now have trending discussion clusters
print(clusters)
```

This will return clustered discussions around your search topic, helping you understand what people are talking about.

### Getting Detailed Cluster Information

```python
from membit import MembitClient

# Step 1. Instantiate your MembitClient
client = MembitClient(api_key="your_api_key_here")

# Step 2. First, find clusters
clusters = client.route_cluster_search(q="climate change")

# Step 3. Get detailed info about the first cluster
cluster_label = clusters["clusters"][0]["label"]
cluster_details = client.route_cluster_info(label=cluster_label, limit=10)

# Step 4. Now you have detailed context about this specific discussion
print(cluster_details)
```

This gives you deeper insights into a specific trending discussion cluster.

### Searching for Individual Posts

```python
from membit import MembitClient

# Step 1. Instantiate your MembitClient
client = MembitClient(api_key="your_api_key_here")

# Step 2. Search for specific social posts
posts = client.post_search(q="machine learning breakthrough", limit=20)

# Step 3. Access individual social media posts
for post in posts.get("posts", []):
    print(f"Post: {post}")
```

Perfect for when you need to find specific posts rather than trending discussions.

## Async Support

The Membit client also supports asynchronous operations for better performance in async applications:

### Async Trending Clusters

```python
import asyncio
from membit import AsyncMembitClient

async def main():
    # Step 1. Instantiate your AsyncMembitClient
    client = AsyncMembitClient(api_key="your_api_key_here")

    # Step 2. Search for trending clusters asynchronously
    clusters = await client.route_cluster_search(q="tech news", limit=5)

    # Step 3. Get cluster details
    if clusters.get("clusters"):
        cluster_info = await client.route_cluster_info(
            label=clusters["clusters"][0]["label"]
        )
        print(cluster_info)

# Run the async function
asyncio.run(main())
```

## Response Formats

The Membit API supports different response formats to suit your needs:

### JSON Format (Default)

```python
from membit import MembitClient

client = MembitClient()
response = client.route_cluster_search(q="space exploration", format="json")
# Returns structured JSON data
```

### LLM-Optimized Format

```python
from membit import MembitClient

client = MembitClient()
response = client.route_cluster_search(q="space exploration", format="llm")
# Returns LLM-friendly formatted text
```

## API Methods

### `route_cluster_search(q, limit=10, format="json", timeout=60)`

Get trending discussions across social platforms. Useful for finding topics of interest and understanding live conversations.

**Parameters:**

- `q` (str): Search query string
- `limit` (int, optional): Maximum number of results to return (default: 10)
- `format` (str, optional): Response format - "json" or "llm" (default: "json")
- `timeout` (int, optional): Request timeout in seconds (default: 60, max: 120)

**Returns:** dict containing trending discussion clusters

### `route_cluster_info(label, limit=10, format="json", timeout=60)`

Dive deeper into a specific trending discussion cluster. Useful for understanding the context and participants of a particular conversation.

**Parameters:**

- `label` (str): Cluster label obtained from `route_cluster_search`
- `limit` (int, optional): Maximum number of results to return (default: 10)
- `format` (str, optional): Response format - "json" or "llm" (default: "json")
- `timeout` (int, optional): Request timeout in seconds (default: 60, max: 120)

**Returns:** dict containing detailed cluster information

### `post_search(q, limit=10, format="json", timeout=60)`

Search for raw social posts. Useful when you need to find specific posts.

**Parameters:**

- `q` (str): Search query string
- `limit` (int, optional): Maximum number of results to return (default: 10)
- `format` (str, optional): Response format - "json" or "llm" (default: "json")
- `timeout` (int, optional): Request timeout in seconds (default: 60, max: 120)

**Returns:** dict containing raw social posts

## Error Handling

The client includes proper error handling:

```python
from membit import MembitClient, MissingAPIKeyError

try:
    # This will raise MissingAPIKeyError if no API key is provided
    client = MembitClient()
    result = client.route_cluster_search("python programming")
except MissingAPIKeyError:
    print("Please provide a valid API key")
except TimeoutError:
    print("Request timed out")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Requirements

- Python >=3.12,<3.13
- requests>=2.25.0 (for sync client)
- httpx>=0.28.1 (for async client)

## Examples

Check out the `examples/` directory for complete working examples:

- `examples/client.py` - Synchronous client usage
- `examples/async_client.py` - Asynchronous client usage

To run the examples:

```bash
export MEMBIT_API_KEY="your_api_key_here"
uv sync
uv run examples/client.py
```

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.

## Contact

For support or questions about the Membit Python client, please reach out to our support team.
