from bs4 import BeautifulSoup
import re
import urllib
from urllib.parse import urljoin
class HtmlParser(object):

    def parse(self,new_url,html_cont):
       if new_url is None or html_cont is None:
           return

       soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
       new_urls=self.get_new_urls(new_url,soup)
       new_data=self.get_new_data(new_url,soup)
       return new_urls,new_data

    def get_new_urls(self, page_url, soup):
        new_urls=set()
        #  /item/python/123
        links=soup.find_all('a',href=re.compile(r'/item/*'))
        for link in links:
            new_url=link['href']
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls


    def get_new_data(self, new_url, soup):
        res_data={}

        # url
        res_data['url']=new_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()

        #  <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
