valid_user_schema = {
    "type": "object",
    "properties": {
        "phone": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "city": {"type": "string"},
            "street": {"type": "string"},
            "home_number": {"type": "string"}
        }
    },
    "required": ["message"]
}
