import urllib.request
import re
from bs4 import BeautifulSoup, SoupStrainer
import lxml
import concurrent.futures

f = open('armorlistLiteralZero2', 'w')


def main():
    iteration = 7294

    for num in range(7294, 20000):  # stopped the program manually at the first range value, so I started it back there

        my_soup = get_html(iteration)

        if (str(my_soup.find(text=re.compile('Armor:'))) == 'None' and
            str(my_soup.find(text=re.compile('Npc Map not available'))) == 'None'):

            f.write("NPC: " + str(iteration) + "---> " + my_soup.title.string.split('-')[0] + "\n")

            for li in my_soup.find_all('li'):
                f.write(li.text + "  ")

            f.write("\n\n")

            iteration += 1

            print("Got:" + str(iteration - 1))

        else:
            iteration += 1

            print("Nope:" + str(iteration - 1))

    f.close()


def get_html(npc_count):  # gets the html sheet from the url given, converts it to a string

    while True:

        try:

            site = "https://db.valkyrie-wow.org/?npc=" + str(npc_count)

            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 '
                              '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

            req = urllib.request.Request(site, headers=hdr)

            page = urllib.request.urlopen(req)

            filterer = SoupStrainer('li')

            soup = BeautifulSoup(page, 'lxml')

            return soup

        except:
            Exception

            print("whoops its fucked\n\n\n ops")

            f.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as e:
    e.map(main())
