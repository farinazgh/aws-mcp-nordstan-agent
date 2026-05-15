import json
import os

import boto3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("nordstan-restaurant-mcp-server")

lambda_client = boto3.client("lambda")

FUNCTION_NAME = os.environ.get("RESTAURANT_FUNCTION_NAME", "nordstan-lambda")


@mcp.tool()
def search_restaurants(
    location: str,
    time: str,
    dietary_preference: str = "vegetarian",
    price_range: str = "moderate",
    requires_availability: bool = True,
) -> dict:
    """
    Search restaurants by location, time,
    dietary preference, price range,
    and availability.
    """

    payload = {
        "location": location,
        "time": time,
        "dietary_preference": dietary_preference,
        "price_range": price_range,
        "requires_availability": requires_availability,
    }

    response = lambda_client.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload).encode("utf-8"),
    )

    response_payload = json.loads(response["Payload"].read())

    return response_payload


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
    )
