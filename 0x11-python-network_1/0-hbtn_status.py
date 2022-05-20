#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    try:
        url = "https://intranet.hbtn.io/status"
        url_intranet = urllib.request.urlopen(url)
        html = url_intranet.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8", "replace")))
    except Exception as err:
        print("Error: ", err)
