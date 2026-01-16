import json
from jsonschema import validate, ValidationError

# Load schemas
with open("schemas/blueprint.schema.json") as f:
    blueprint_schema = json.load(f)

with open("schemas/ethical.schema.json") as f:
    ethical_schema = json.load(f)

# Load data
with open("outputs/blueprint.json") as f:
    blueprint = json.load(f)

# Example JSON with ethical parameters (can also be saved in outputs/ethical.json)
ethical_data = {
    "privacy": "medium",
    "bias": "low",
    "transparency": "high",
    "harm_potential": "low"
}

# Validate blueprint
try:
    validate(instance=blueprint, schema=blueprint_schema)
    print("Blueprint is valid ")
except ValidationError as e:
    print("Blueprint validation error ", e)

# Validate ethical JSON
try:
    validate(instance=ethical_data, schema=ethical_schema)
    print("Ethical JSON is valid ")
except ValidationError as e:
    print("Ethical JSON validation error ", e)
