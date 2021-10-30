import re


def get_house(post_id, post_content):
    # for posts which don't have tag in content
    force_list = {
        "S": [],
        "R": [],
        "H": [],
        "G": []
    }

    if re.search("slytherin2021", post_content, re.IGNORECASE) or post_id in force_list["S"]:
        return "S"
    if re.search("Ravenclaw2021", post_content, re.IGNORECASE) or post_id in force_list["R"]:
        return "R"
    if re.search("hufflepuff2021", post_content, re.IGNORECASE) or post_id in force_list["H"]:
        return "H"
    if re.search("gryffindor2021", post_content, re.IGNORECASE) or post_id in force_list["G"]:
        return "G"
    print("Couldn't classify post id " + post_id + " with content " + post_content)
    return "X"
