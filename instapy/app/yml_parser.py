
import yaml
from urllib.request import urlopen

link = "https://raw.githubusercontent.com/dominikpeter/InstaBot/master/instapy/app/config.yml"

def parse_yml(path):

    f = urlopen(link)
    config = f.read()

    try:
        return yaml.safe_load(config)
    except yaml.YAMLError as exc:
        print(exc)
        return None


    


