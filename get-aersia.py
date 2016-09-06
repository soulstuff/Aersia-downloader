#!python3

import requests
import os.path
from html.parser import HTMLParser


URL = 'http://vip.aersia.net/mu/'


class VipScrapper(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if (attr[1][0] == "?"
                        or attr[1][0] == "!"
                        or attr[1][0] == "/"
                        or attr[1][-1] == "/"):
                    print("",
                          attr[1],
                          " is not an avalible link, skipping...")
                else:
                    print("Downloading ", URL+attr[1], "...")
                    if os.path.isfile(attr[1]):
                        print("The file already exists, skipping...")
                    else:
                        r = requests.get(URL+attr[1])
                        with open(attr[1], "wb") as song:
                            song.write(r.content)


if __name__ == "__main__":

    r = requests.get(URL)
    parser = VipScrapper()
    parser.feed(r.text)
