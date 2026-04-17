import json

with open("server2.json", "r") as f:
    server2 = json.load(f)

# print(type(server2))
#
# print(server2["server1"])
# print(server2["server2"])

for key, value in server2.items():
    print(f"key and value: '{key}' = '{value}'")
    for sub_key, sub_val in value.items():
        print(f"sub_key: '{sub_key}' = '{sub_val}'")