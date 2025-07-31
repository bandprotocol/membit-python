class MissingAPIKeyError(Exception):
    def __init__(self):
        super().__init__(
            "No API key provided. Please provide the api_key attribute or set the MEMBIT_API_KEY environment variable."
        )
