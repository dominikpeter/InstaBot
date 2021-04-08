
import os
from yml_parser import parse_yml
import random

INSTA_USER = os.getenv("INSTA_USER")
INSTA_PW = os.getenv("INSTA_PW")
CONFIG_LINK = "https://raw.githubusercontent.com/dominikpeter/InstaBot/master/instapy/app/config.yml"

YML_CONFIG = parse_yml(CONFIG_LINK)
DONT_LIKE = YML_CONFIG["dont_like"]
FRIEND_LIST = YML_CONFIG["friends"]
USER_INTERACTS = YML_CONFIG["user_interacts"]
LIKES = YML_CONFIG["likes"]
LIKES_SAMPLE = YML_CONFIG["likes_sample"]
RANDOM_LIKES = random.sample(YML_CONFIG["random_likes"], LIKES_SAMPLE)
LIKES = list(set(LIKES + RANDOM_LIKES))
LOCATIONS = YML_CONFIG["locations"]
PHOTO_COMMENTS = YML_CONFIG["photo_comments"]
MAX_FOLLOWERS = YML_CONFIG["max_followers"]
MIN_FOLLOWERS = YML_CONFIG["min_fallowers"]
MIN_FOLLOWING = YML_CONFIG["min_following"]
MIN_LIKES = YML_CONFIG["min_likes"]
MAX_LIKES = YML_CONFIG["max_likes"]
MIN_TO_FOLLOW = YML_CONFIG["min_to_follow"]
MAX_TO_FOLLOW = YML_CONFIG["max_to_follow"]
PODS = YML_CONFIG["pods"]