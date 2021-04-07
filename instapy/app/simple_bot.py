
import random
import os
import time

from instapy import InstaPy
from instapy import smart_run


INSTA_USER = os.getenv("INSTA_USER")
INSTA_PW = os.getenv("INSTA_PW")


dont_like = ["nude", "girl", "hot", "sex"]
friend_list = ["amytolja", "vireaksoeur"]
likes = ["sunrise", "sunset", "drone",
         "droneshot", "dronephotography", "rigi",
         "hallwilersee", "sempach", "standuppaddle",
         "mountainbike", "switzerland", "sonnenaufgabg",
         "sonnenuntergang", "drohne", "see", "aargau",
         "sempachersee", "water", "calm", "relax", "luzern",
         "bern", "aarau", "wandern", "berge", "droneoftheday", 
         "nature", "landscape", "natur", "wanderlust", "#lakelife"]


i = 1
while 1==1:

    print(f"Starting run {i}")

    session = InstaPy(username=INSTA_USER,
                password=INSTA_PW,
                headless_browser=True)

    with smart_run(session):

        """ Activity flow """
        # general settings
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=45900,
                                        min_followers=20,
                                        min_following=20)

        session.set_dont_include(friend_list)
        session.set_dont_like(dont_like)
        session.like_by_tags(likes, amount=100)

    session.stop()

    i += 1

    sleep_time = random.randint(1800,14400)
    print(f"Sleeping for {sleep_time} seconds")

    time.sleep(sleep_time)