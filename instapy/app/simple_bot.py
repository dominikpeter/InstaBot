
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
likes_sample = yml_config["likes_sample"]
random_likes = random.sample(yml_config["random_likes"], likes_sample)
likes = list(set(likes + random_likes))
locations = yml_config["locations"]
photo_comments = yml_config["photo_comments"]
max_followers = yml_config["max_followers"]
min_followers = yml_config["min_fallowers"]
min_following = yml_config["min_following"]
min_likes = yml_config["min_likes"]
max_likes = yml_config["max_likes"]
min_to_follow = yml_config["min_to_follow"]
max_to_follow = yml_config["max_to_follow"]
pods = yml_config["pods"]


session = InstaPy(username=INSTA_USER,
                  password=INSTA_PW,
                  headless_browser=True)

with smart_run(session):

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=max_followers,
                                    min_followers=min_followers,
                                    min_following=min_following)

    session.set_user_interact(amount=2, randomize=True, percentage=60)

    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    session.set_dont_include(friend_list)
    session.set_dont_like(dont_like)

    session.like_by_tags(likes,
                         amount=random.randint(min_likes, max_likes),
                         interact=True)

    session.like_by_locations(locations,
                              amount=random.randint(min_likes, max_likes),
                              randomize=True)

    session.unfollow_users(amount=random.randint(min_to_follow, max_to_follow),
                           instapy_followed_enabled=True,
                           instapy_followed_param="all",
                           style="FIFO",
                           unfollow_after=90 * 60 * 60,
                           sleep_delay=600)

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(photo_comments, media='Photo')

    for pod in pods:
        session.join_pods(topic=pod)
