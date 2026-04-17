import json

with open("server2.json", "r") as f:
    json_str = f.read() # error the json object must be str,bytes or bytearray

print(type(server2))

print(server2["server1"])
print(server2["server2"])

for key, value in server2.items():
    print(key, value)