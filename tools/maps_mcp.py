from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MultiServerMCPClient(
    {
        "maps": {
            "transport": "streamable_http",
            "url": "https://mapstools.googleapis.com/mcp",
            "headers": {
                "X-Goog-Api-Key": os.getenv('MAPS_API_KEY'),
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream"
            }
        }
    }
)