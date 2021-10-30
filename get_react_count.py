import requests


# "https://graph.facebook.com/v12.0/572180267231316_572181003897909/reactions?summary=total_count&access_token="
def get_react_count(post_id, access_token):
    url = "https://graph.facebook.com/v12.0/"
    url += post_id + "/reactions?summary=total_count&access_token=" + access_token
    print("URL = " + url)
    r = requests.get(url)
    r_dictionary = r.json()
    return r_dictionary["summary"]["total_count"]
