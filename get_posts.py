import requests


# "https://graph.facebook.com/v12.0/572180267231316/feed?since=1635447600&until=1638126000&access_token="
def get_posts(group_id, start_ts, end_ts, access_token):
    url = "https://graph.facebook.com/v12.0/"
    url += group_id + "/feed?since=" + start_ts + "&until=" + end_ts + "&access_token=" + access_token
    print("URL = " + url)
    r = requests.get(url)
    r_dictionary = r.json()
    posts = {}
    for post in r_dictionary.get("data"):
        posts[post.get("id")] = post
        if "message" not in post:
            post["message"] = "NO MESSAGE IN POST"
    return posts
