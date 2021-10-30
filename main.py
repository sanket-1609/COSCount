from get_posts import get_posts
from get_react_count import get_react_count
from get_house import get_house

# "https://graph.facebook.com/v12.0/572180267231316/feed?since=1635447600&until=1638126000&access_token="
group_id = "572180267231316"  # todo CHANGE this
access_token = "<ACCESS TOKEN>"  # todo FILL THIS
since_ts = "1635447600"  # 28Oct 7AM GMT
until_ts = "1638126000"  # 28Nov 7AM GMT

posts = get_posts(group_id, since_ts, until_ts, access_token)
print(posts)

for post_id, post in posts.items():
    react_count = get_react_count(post_id, access_token)
    post["reacts"] = react_count
    house = get_house(post_id, post.get("message"))
    post["house"] = house

print(posts)
