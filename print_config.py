import json

# Read the JSON configuration file
with open("entra-id-atr-map.json", "r") as file:
    config = json.load(file)

# Replace escaped characters with actual newlines and tabs
expression = config["expression"].replace("\\n", "\n").replace("\\t", "\t")

# Print the well-formatted JSON configuration
print(json.dumps({"expression": expression}, indent=4))
