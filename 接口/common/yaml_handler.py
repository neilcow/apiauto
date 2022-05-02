
import yaml


class YamlConfig(object):
    def __init__(self):
        pass

    def read_yaml(self, file, encoding='utf-8'):
        with open(file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self):
        pass


if __name__ == '__main__':
    ya = YamlConfig()
    print(ya.read_yaml('api.yaml'))


