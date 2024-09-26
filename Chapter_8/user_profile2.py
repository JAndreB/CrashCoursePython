def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'enstein', location='princeton',\
field= 'physics')

me = build_profile('mike', 'stanlee', location='paradise', field='unknown',\
terrace= 'monkey', life= 'treehouse', home= 'zebra')

print(user_profile)
print(me)