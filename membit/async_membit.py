import os
from typing import Optional, Literal

import httpx

from .errors import MissingAPIKeyError
from .constants import MEMBIT_API_URL


class AsyncMembitClient:
    """
    An async client for the Membit API.

    Provides async methods for:
    - clusters_search: Get trending discussions across social platforms
    - clusters_info: Dive deeper into specific trending discussion clusters
    - posts_search: Search for raw social posts
    """

    def __init__(self, api_key: Optional[str] = None, api_url: Optional[str] = None):
        if api_key is None:
            api_key = os.getenv("MEMBIT_API_KEY")

        if not api_key:
            raise MissingAPIKeyError()

        self.api_url = api_url or MEMBIT_API_URL
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "X-Membit-Api-Key": self.api_key,
        }
        self._client_creator = lambda: httpx.AsyncClient(
            base_url=self.api_url,
            headers=self.headers,
        )

    async def route_cluster_search(
        self,
        q: str,
        limit: int = 10,
        format: Literal["json", "llm"] = "json",
        timeout: int = 60,
    ) -> dict:
        """
        Get trending discussions across social platforms: useful for finding topics of interest and understanding live conversations.

        Args:
            q: Search query string
            limit: Maximum number of results to return (default: 10)
            format: Response format - "json" or "llm" (default: "json")
            timeout: Request timeout in seconds (default: 60, max: 120)

        Returns:
            dict: Search results containing trending discussion clusters
        """
        timeout = min(timeout, 120)
        data = {"q": q, "limit": limit, "format": format}

        async with self._client_creator() as client:
            try:
                response = await client.get(
                    "/clusters/search", params=data, timeout=timeout
                )
            except httpx.TimeoutException:
                raise TimeoutError(timeout)

            if response.status_code == 200:
                return response.json()

            raise response.raise_for_status()

    async def route_cluster_info(
        self,
        label: str,
        limit: int = 10,
        format: Literal["json", "llm"] = "json",
        timeout: int = 60,
    ) -> dict:
        """
        Dive deeper into a specific trending discussion cluster: useful for understanding the context and participants of a particular conversation (requires a cluster label from `clusters_search`).

        Args:
            label: Cluster label obtained from clusters_search
            limit: Maximum number of results to return (default: 10)
            format: Response format - "json" or "llm" (default: "json")
            timeout: Request timeout in seconds (default: 60, max: 120)

        Returns:
            dict: Detailed information about the specific cluster
        """
        timeout = min(timeout, 120)

        data = {"label": label, "limit": limit, "format": format}

        async with self._client_creator() as client:
            try:
                response = await client.get(
                    "/clusters/info", params=data, timeout=timeout
                )
            except httpx.TimeoutException:
                raise TimeoutError(timeout)

            if response.status_code == 200:
                return response.json()

            response.raise_for_status()

    async def post_search(
        self,
        q: str,
        limit: int = 10,
        format: Literal["json", "llm"] = "json",
        timeout: int = 60,
    ) -> dict:
        """
        Search for raw social posts: useful when you need to find specific posts (not recommended for finding trending discussions).

        Args:
            q: Search query string
            limit: Maximum number of results to return (default: 10)
            format: Response format - "json" or "llm" (default: "json")
            timeout: Request timeout in seconds (default: 60, max: 120)

        Returns:
            dict: Search results containing raw social posts
        """
        timeout = min(timeout, 120)

        data = {"q": q, "limit": limit, "format": format}

        async with self._client_creator() as client:
            try:
                response = await client.get(
                    "/posts/search", params=data, timeout=timeout
                )
            except httpx.TimeoutException:
                raise TimeoutError(timeout)

            if response.status_code == 200:
                return response.json()

            raise response.raise_for_status()
