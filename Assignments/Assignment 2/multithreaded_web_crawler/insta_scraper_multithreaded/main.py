# With Reeference to this video tutorial - https://www.youtube.com/watch?v=qQDB6SE0a9c

import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count


def get_links(url):
    curr_list = url
    all_links = []
    response = requests.get(curr_list)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    curr_element = soup.select('p+table td:nth-child(2) > a, p+table td:nth-child(1) > a:nth-child(1)')
    for link_element in curr_element:
        link = link_element.get("href")
        link = urljoin(curr_list, link)
        all_links.append(link)

    return all_links


def fetch1(link):
    #response = requests.get(link)
    # response = s.get(link)
    '''filename = './output/' + link.split('/')[-1] + '.html'
    with open(filename, 'wb') as f:
        f.write(response.content)'''
    print('.', end = "", flush = True)
    
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_circulating_currencies"
    links = get_links(url)
    print(f"Total Pages: {len(links)}")
    start_time = time.time()
    # This for loop is to be optimized
    # s = requests.Session()
    # with Pool(cpu_count()) as p:
     #   p.map(fetch, links)
    #----------------------
    '''for link in links:
        fetch(link, s)'''
    #----------------------

    # Threading
    with ThreadPoolExecutor(max_workers = 20) as executor:
        executor.map(fetch1, links)
    duration = time.time() - start_time
    print(f"Downloaded {len(links)} links in {duration} seconds")
