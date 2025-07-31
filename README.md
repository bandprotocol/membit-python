# Membit Python Client

[![PyPI - Downloads](https://img.shields.io/pypi/dm/membit-python)](https://pypi.org/project/membit-python/)
[![License](https://img.shields.io/github/license/bandprotocol/membit-python)](https://github.com/bandprotocol/membit-python/blob/main/LICENSE)

The Membit Python client provides powerful social media analytics and monitoring capabilities for your Python applications. Easily integrate trending discussion discovery, cluster analysis, and social post search with a simple and intuitive API.

## Installation

```bash
pip install membit-python
```

Or with uv:

```bash
uv add membit-python
```

## Quick Start

### Basic Usage

```python
from membit import MembitClient

# Initialize the client with API key
client = MembitClient(api_key="your_api_key_here")

# Or use environment variable MEMBIT_API_KEY
# client = MembitClient()

# Search for trending discussion clusters
clusters = client.cluster_search("artificial intelligence", limit=5)
print(clusters)
```

## Features

### 🔥 Trending Discussion Clusters

Find and analyze trending discussions across social platforms with intelligent clustering.

### 🔍 Deep Cluster Analysis

Dive deeper into specific discussions to understand context and participants.

### 📱 Social Post Search

Search for individual social media posts on specific topics.

### ⚡ Async Support

Full async/await support for high-performance applications.

### 📊 Multiple Response Formats

Get data in JSON format for applications or LLM-optimized text for AI workflows.

## Usage Examples

### Finding Trending Discussion Clusters

```python
from membit import MembitClient

# Initialize client with API key
client = MembitClient(api_key="your_api_key_here")
# Or use environment variable MEMBIT_API_KEY
# client = MembitClient()

# Search for trending clusters
clusters = client.cluster_search("artificial intelligence", limit=5)

# clusters is a dict containing trending discussion clusters
for cluster in clusters.get("clusters", []):
    print(f"Cluster: {cluster['label']}")
```

### Getting Detailed Cluster Information

```python
from membit import MembitClient

# Initialize client with API key
client = MembitClient(api_key="your_api_key_here")

# First, find clusters
clusters = client.cluster_search("climate change")

# Get detailed info about the first cluster
if clusters.get("clusters"):
    cluster_label = clusters["clusters"][0]["label"]
    cluster_details = client.cluster_info(label=cluster_label, limit=10)
    print(cluster_details)
```

### Searching for Individual Posts

```python
from membit import MembitClient

# Initialize client with API key
client = MembitClient(api_key="your_api_key_here")

# Search for specific social posts
posts = client.post_search("machine learning breakthrough", limit=20)

# Access individual social media posts
for post in posts.get("posts", []):
    print(f"Post: {post}")
```

### Using Different Response Formats

```python
from membit import MembitClient

# Initialize client with API key
client = MembitClient(api_key="your_api_key_here")

# Get JSON response (default)
json_response = client.cluster_search("space exploration", output_format="json")
# Returns: dict with structured data

# Get LLM-optimized text response
llm_response = client.cluster_search("space exploration", output_format="llm")
# Returns: str with formatted text optimized for AI processing
```

## Async Support

For applications that need high performance or handle multiple concurrent requests:

```python
import asyncio
from membit import AsyncMembitClient

async def analyze_topics():
    client = AsyncMembitClient(api_key="your_api_key_here")

    # Search for trending clusters asynchronously
    clusters = await client.cluster_search("tech news", limit=5)

    # Get detailed info for multiple clusters concurrently
    if clusters.get("clusters"):
        tasks = [
            client.cluster_info(label=cluster["label"])
            for cluster in clusters["clusters"][:3]
        ]
        cluster_details = await asyncio.gather(*tasks)

        for details in cluster_details:
            print(details)

# Run the async function
asyncio.run(analyze_topics())
```

## API Reference

### `MembitClient(api_key=None, api_url=None)`

Initialize the Membit client.

**Parameters:**

- `api_key` (str, optional): Your Membit API key. If not provided, uses `MEMBIT_API_KEY` environment variable.
- `api_url` (str, optional): Custom API URL. Uses default Membit API URL if not provided.

---

### `cluster_search(q, limit=10, output_format="json", timeout=60)`

Get trending discussions across social platforms. Useful for finding topics of interest and understanding live conversations.

**Parameters:**

- `q` (str): Search query string
- `limit` (int, optional): Maximum number of results to return (default: 10)
- `output_format` (str, optional): Response format - `"json"` or `"llm"` (default: `"json"`)
- `timeout` (int, optional): Request timeout in seconds (default: 60, max: 120)

**Returns:**

- `dict`: Trending discussion clusters (when `output_format="json"`)
- `str`: Formatted text response (when `output_format="llm"`)

---

### `cluster_info(label, limit=10, output_format="json", timeout=60)`

Dive deeper into a specific trending discussion cluster. Useful for understanding the context and participants of a particular conversation.

**Parameters:**

- `label` (str): Cluster label obtained from `cluster_search`
- `limit` (int, optional): Maximum number of results to return (default: 10)
- `output_format` (str, optional): Response format - `"json"` or `"llm"` (default: `"json"`)
- `timeout` (int, optional): Request timeout in seconds (default: 60, max: 120)

**Returns:**

- `dict`: Detailed cluster information (when `output_format="json"`)
- `str`: Formatted text response (when `output_format="llm"`)

---

### `post_search(q, limit=10, output_format="json", timeout=60)`

Search for raw social posts. Useful when you need to find specific posts (not recommended for finding trending discussions).

**Parameters:**

- `q` (str): Search query string
- `limit` (int, optional): Maximum number of results to return (default: 10)
- `output_format` (str, optional): Response format - `"json"` or `"llm"` (default: `"json"`)
- `timeout` (int, optional): Request timeout in seconds (default: 60, max: 120)

**Returns:**

- `dict`: Raw social posts (when `output_format="json"`)
- `str`: Formatted text response (when `output_format="llm"`)

## Error Handling

The client includes comprehensive error handling:

```python
from membit import MembitClient, MissingAPIKeyError

try:
    # Initialize client with API key
    client = MembitClient(api_key="your_api_key_here")

    result = client.cluster_search("python programming")

except MissingAPIKeyError:
    print("Please provide a valid API key")

except TimeoutError:
    print("Request timed out")

except Exception as e:
    print(f"An error occurred: {e}")
```

## Requirements

- **Python:** >=3.10
- **Dependencies:**
  - `requests>=2.25.0` (for synchronous client)
  - `httpx>=0.28.1` (for asynchronous client)

## Examples

Complete working examples are available in the `examples/` directory:

- [`examples/client.py`](examples/client.py) - Synchronous client usage
- [`examples/async_client.py`](examples/async_client.py) - Asynchronous client usage

### Running Examples

```bash
# Set your API key
export MEMBIT_API_KEY="your_api_key_here"

# Install dependencies
uv sync

# Run synchronous example
uv run examples/client.py

# Run asynchronous example
uv run examples/async_client.py
```

## Development

### Installing for Development

```bash
git clone <repository-url>
cd membit-python
uv sync
```

### Running Tests

```bash
uv run pytest
```

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For support or questions about the Membit Python client, please reach out to our support team.
