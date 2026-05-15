import json
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

TOOLS = [
    {
        "type": "function",
        "name": "search_restaurants",
        "description": "Search restaurants by location, time, dietary preference, price range, and availability.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "time": {"type": "string"},
                "dietary_preference": {"type": "string"},
                "price_range": {"type": "string"},
                "requires_availability": {"type": "boolean"},
            },
            "required": ["location", "time"],
        },
    }
]


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    prompt = body.get("prompt", "")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        tools=TOOLS,
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": response.output_text}),
    }
