
import yaml
from urllib.request import urlopen


def parse_yml(link):

    f = urlopen(link)
    config = f.read()

    try:
        return yaml.safe_load(config)
    except yaml.YAMLError as exc:
        print(exc)
        return None


    


