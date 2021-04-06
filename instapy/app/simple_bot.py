
import random
import os
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
         "sonnenuntergang", "drohne", "see", "aargau"]

session = InstaPy(username=INSTA_USER, password=INSTA_PW, headless_browser=True)
with smart_run(session):

    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(friend_list)
    session.set_dont_like(dont_like)
    session.like_by_tags(likes, amount=500)