import yaml

with open("servers.yaml", 'r') as file:
    servers = yaml.safe_load(file) #

print(type(servers))

