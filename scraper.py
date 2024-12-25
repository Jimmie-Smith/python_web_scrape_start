import pprint

import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
b_soup = BeautifulSoup(response.text, 'html.parser')
titles =  b_soup.select('.titleline')
links = b_soup.select('.titleline > a')
votes = b_soup.select('.score')


def sort_stories_by_votes(site_list):
    return sorted(site_list, key= lambda x: x['points'], reverse=True)

def create_custom_site(links, votes):
    site = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        if points > 100:
            site.append({'title': title, 'link': href, 'points': points})
    return sort_stories_by_votes(site)

pprint.pprint(create_custom_site(links, votes))