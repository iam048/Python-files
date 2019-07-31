import requests
from bs4 import BeautifulSoup
file = open('proxy.txt', 'w')
url = ['https://free-proxy-list.net/']#'https://www.google.com']
#print "\n [*] Collecting Proxies from " + url[0]
#soup_1 = BeautifulSoup(requests.get(url[0]).content, 'lxml')
for i in range(len(url)):
    print ("\n [*] Collecting Latest Proxies From " + url[i]+'\n')
    soup =  BeautifulSoup(requests.get(url[i]).content, 'lxml')
    for data in soup.find('tbody').findAll('tr')[:50]:
        ip = data.find('td').text
        port = data.find('td').next_sibling.text
        file.write(ip+':'+port+'\n')
    print('[X] Done')
    file.close()
