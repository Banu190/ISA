import json
from jsonschema import validate, ValidationError

# Загружаем схемы
with open("schemas/blueprint.schema.json") as f:
    blueprint_schema = json.load(f)

with open("schemas/ethical.schema.json") as f:
    ethical_schema = json.load(f)

# Загружаем данные
with open("outputs/blueprint.json") as f:
    blueprint = json.load(f)

# Пример JSON с этическими параметрами (можно вынести в outputs/ethical.json)
ethical_data = {
    "privacy": "medium",
    "bias": "low",
    "transparency": "high",
    "harm_potential": "low"
}

# Проверяем blueprint
try:
    validate(instance=blueprint, schema=blueprint_schema)
    print("Blueprint is valid ✅")
except ValidationError as e:
    print("Blueprint validation error ❌", e)

# Проверяем этику
try:
    validate(instance=ethical_data, schema=ethical_schema)
    print("Ethical JSON is valid ✅")
except ValidationError as e:
    print("Ethical JSON validation error ❌", e)
