def generate_hashtag(s):
    hashtag_str = "#"
    operating_str = s.split(" ")
    for st in operating_str:
        if st != " ":
            hashtag_str += st.capitalize()
    if len(hashtag_str) > 140:
        return False
    if hashtag_str == "#":
        return False
    return hashtag_str

