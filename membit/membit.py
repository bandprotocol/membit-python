import os
from typing import Literal, overload
import requests

from .errors import MissingAPIKeyError
from .constants import MEMBIT_API_URL


class MembitClient:
    """
    A client for the Membit API.
    """

    def __init__(self, api_key: str | None = None, api_url: str | None = None):
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

    def _parse_response(self, response: requests.Response) -> dict | str:
        """Parse response based on content type."""
        if response.status_code == 200:
            content_type = response.headers.get("content-type", "").lower()
            match content_type:
                case ct if "application/json" in ct:
                    return response.json()
                case ct if "text/plain" in ct:
                    return response.text
                case _:
                    raise RuntimeError(f"Unknown content type: {content_type}")

        response.raise_for_status()

    @overload
    def cluster_search(
        self,
        q: str,
        *,
        limit: int = 10,
        output_format: Literal["json"] = "json",
        timeout: int = 60,
    ) -> dict: ...

    @overload
    def cluster_search(
        self,
        q: str,
        *,
        limit: int = 10,
        output_format: Literal["llm"] = "llm",
        timeout: int = 60,
    ) -> str: ...

    def cluster_search(
        self,
        q: str,
        *,
        limit: int = 10,
        output_format: Literal["json", "llm"] = "json",
        timeout: int = 60,
    ) -> dict | str:
        """
        Get trending discussions across social platforms: useful for finding topics of interest and understanding live conversations.

        Args:
            q: Search query string
            limit: Maximum number of results to return (default: 10)
            output_format: Response format - "json" or "llm" (default: "json")
            timeout: Request timeout in seconds (default: 60, max: 120)

        Returns:
            dict: Search results containing trending discussion clusters (when output_format="json")
            str: Formatted text response (when format="llm")

        Raises:
            ValueError: If timeout exceeds 120 seconds
        """
        if timeout > 120:
            raise ValueError("Timeout cannot exceed 120 seconds")

        data = {
            "q": q,
            "limit": limit,
            "format": output_format,
        }

        try:
            response = requests.get(
                self.api_url + "/clusters/search",
                params=data,
                headers=self.headers,
                timeout=timeout,
            )
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out")

        return self._parse_response(response)

    @overload
    def cluster_info(
        self,
        label: str,
        *,
        limit: int = 10,
        output_format: Literal["json"] = "json",
        timeout: int = 60,
    ) -> dict: ...

    @overload
    def cluster_info(
        self,
        label: str,
        *,
        limit: int = 10,
        output_format: Literal["llm"] = "llm",
        timeout: int = 60,
    ) -> str: ...

    def cluster_info(
        self,
        label: str,
        *,
        limit: int = 10,
        output_format: Literal["json", "llm"] = "json",
        timeout: int = 60,
    ) -> dict | str:
        """
        Dive deeper into a specific trending discussion cluster: useful for understanding the context and participants of a particular conversation (requires a cluster label from `clusters_search`).

        Args:
            label: Cluster label obtained from clusters_search
            limit: Maximum number of results to return (default: 10)
            output_format: Response format - "json" or "llm" (default: "json")
            timeout: Request timeout in seconds (default: 60, max: 120)

        Returns:
            dict: Cluster information (when format="json")
            str: Formatted text response (when format="llm")

        Raises:
            ValueError: If timeout exceeds 120 seconds
        """
        if timeout > 120:
            raise ValueError("Timeout cannot exceed 120 seconds")

        data = {
            "label": label,
            "limit": limit,
            "format": output_format,
        }

        try:
            response = requests.get(
                self.api_url + "/clusters/info",
                params=data,
                headers=self.headers,
                timeout=timeout,
            )
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out")

        return self._parse_response(response)

    @overload
    def post_search(
        self,
        q: str,
        *,
        limit: int = 10,
        output_format: Literal["json"] = "json",
        timeout: int = 60,
    ) -> dict: ...

    @overload
    def post_search(
        self,
        q: str,
        *,
        limit: int = 10,
        output_format: Literal["llm"] = "llm",
        timeout: int = 60,
    ) -> str: ...

    def post_search(
        self,
        q: str,
        *,
        limit: int = 10,
        output_format: Literal["json", "llm"] = "json",
        timeout: int = 60,
    ) -> dict | str:
        """
        Search for raw social posts: useful when you need to find specific posts (not recommended for finding trending discussions).

        Args:
            q: Search query string
            limit: Maximum number of results to return (default: 10)
            output_format: Response format - "json" or "llm" (default: "json")
            timeout: Request timeout in seconds (default: 60, max: 120)

        Returns:
            dict: Search results containing raw social posts (when format="json")
            str: Formatted text response (when format="llm")

        Raises:
            ValueError: If timeout exceeds 120 seconds
        """
        if timeout > 120:
            raise ValueError("Timeout cannot exceed 120 seconds")

        data = {
            "q": q,
            "limit": limit,
            "format": output_format,
        }

        try:
            response = requests.get(
                self.api_url + "/posts/search",
                params=data,
                headers=self.headers,
                timeout=timeout,
            )
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out")

        return self._parse_response(response)
