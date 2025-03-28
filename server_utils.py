# server_utils.py

def get_homepage_content():
    with open("index.html", 'r') as homepage:
        return homepage.read()
