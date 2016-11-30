from bs4 import BeautifulSoup
from urllib2 import urlopen, Request

nb_ep_flash_vue = 6

req = Request('http://streamay.bz/series/flash-2014',headers={'User-Agent': 'Magic Browser'})
soup = BeautifulSoup(urlopen(req), "html.parser")

saisons = soup.find_all('div', class_='saisons_episodes')
for last_saison in saisons:
	pass
episodes = last_saison.find_all('a', class_='item')

if len(episodes) > nb_ep_flash_vue:
	for last_episode in episodes: 
		pass
	print last_episode['href']



