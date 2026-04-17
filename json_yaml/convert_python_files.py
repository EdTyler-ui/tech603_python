import json


# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
# print(servers_dict)

json_str = json.dumps(servers_dict, indent=4)
print(json_str)

with open("servers_dict.json", "w") as f:
    json.dump(servers_dict, f, indent=4)
