
import random
import os
import time

from instapy import InstaPy
from instapy import smart_run
from yml_parser import parse_yml


INSTA_USER = os.getenv("INSTA_USER")
INSTA_PW = os.getenv("INSTA_PW")


yml_config = parse_yml("./app/config.yml")


dont_like = yml_config["dont_like"]
friend_list = yml_config["friends"]
likes = yml_config["likes"]
max_followers = yml_config["max_followers"]
min_followers = yml_config["min_fallowers"]
min_following = yml_config["min_following"]
n_likes = yml_config["n_likes"]


session = InstaPy(username=INSTA_USER,
                  password=INSTA_PW,
                  headless_browser=True)

with smart_run(session):

    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=max_followers,
                                    min_followers=min_followers,
                                    min_following=min_following)

    session.set_dont_include(friend_list)
    session.set_dont_like(dont_like)
    session.like_by_tags(likes, amount=n_likes)
