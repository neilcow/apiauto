import yaml

f = open('api.yaml', encoding='utf-8')
data = yaml.load(f.read(), Loader=yaml.FullLoader)
print(data)
f.close()

