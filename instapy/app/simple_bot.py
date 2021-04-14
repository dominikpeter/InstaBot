
import random
import os
import time
from datetime import datetime

from instapy import InstaPy
from instapy import smart_run
from const import *

print(YML_CONFIG)

start = datetime.now()


session = InstaPy(username=INSTA_USER,
                  password=INSTA_PW,
                  headless_browser=True)

session.logger.info(YML_CONFIG)

with smart_run(session):

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=MAX_FOLLOWERS,
                                    min_followers=MIN_FOLLOWERS,
                                    min_following=MIN_FOLLOWING)

    session.set_user_interact(amount=USER_INTERACTS, randomize=True, percentage=50)

#    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    session.set_dont_include(FRIEND_LIST)
    session.set_dont_like(DONT_LIKE)

    session.like_by_tags(LIKES,
                         amount=random.randint(MIN_LIKES, MAX_LIKES),
                         interact=True)

    session.like_by_locations(LOCATIONS,
                              amount=random.randint(MIN_LIKES, MAX_LIKES),
                              randomize=True)

 #   session.unfollow_users(amount=random.randint(MIN_TO_FOLLOW, MAX_TO_FOLLOW),
 #                          instapy_followed_enabled=True,
 #                          instapy_followed_param="all",
 #                          style="FIFO",
 #                          unfollow_after=90 * 60 * 60,
 #                          sleep_delay=600)

    session.set_do_comment(enabled=True, percentage=50)
    session.set_comments(PHOTO_COMMENTS, media="Photo")

#    for pod in PODS:
#        session.join_pods(topic=pod)

minutes_diff = (datetime.now() - start).total_seconds() / 60.0
session.logger.info(f"Duration = {minutes_diff} minutes")

