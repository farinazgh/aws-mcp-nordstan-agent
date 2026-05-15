def lambda_handler(event, context):
    return {
        "restaurants": [
            {
                "name": "Green Nordstan Kitchen",
                "location": "Nordstan, Gothenburg",
                "vegetarian_options": True,
                "available_at": event.get("time"),
                "price_range": "moderate",
                "notes": "Vegetarian bowls, salads, and casual dinner options.",
            },
            {
                "name": "Veggie Fika & Food",
                "location": "Near Nordstan",
                "vegetarian_options": True,
                "available_at": event.get("time"),
                "price_range": "budget",
                "notes": "Simple vegetarian food, good for quick dinner.",
            },
        ]
    }
