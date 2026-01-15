import json
import jsonschema
from jsonschema import validate

# Load the schema and blueprint
with open("schemas/blueprint.schema.json") as f:
    schema = json.load(f)

with open("outputs/blueprint.json") as f:
    blueprint = json.load(f)

# Validation
try:
    validate(instance=blueprint, schema=schema)
    print(" JSON is valid")
except jsonschema.exceptions.ValidationError as e:
    print(" JSON error:", e)
