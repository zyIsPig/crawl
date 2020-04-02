import scrapy
import json
from myfirstSpider.spiders.url_constructor import github_search_url
import time
from myfirstSpider.spiders.header_constructor import header_construct
import re
from scrapy.downloadermiddlewares import retry

class crawlRepo(scrapy.Spider):
    token='92863e9ab09a1f3e1bac7a918f9edbf63b995fc4'
    token1='e1421978758ce779d82f7ebc622c9a8e5e861887'
    name = 'repo_crawler'
    url_list = []


    # headers1={
    #     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
    #
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #     'Accept-Language': 'en',
    #     'Authorization': 'token e1421978758ce779d82f7ebc622c9a8e5e861887'
    # }


    def __init__(self):
        self.url_list=[]




    def start_requests(self):
        urls=[]
        sta_page=1
        end_page=2

        self.log("let's begin.........")
        while sta_page<=end_page:

            test1 = github_search_url(q='library', language='java', sort='stars',page=sta_page,per_page=100)
            aaa = test1.construct()
            # print(aaa)
            urls.append(aaa)

            head_temp=header_construct(sta_page%2+1)


            for url in urls:
                print('...........')
                print(url)

                yield scrapy.Request(url=url,headers=head_temp,callback=self.parse,errback=self.err)


            sta_page+=1

            time.sleep(1)


        time.sleep(3)
        self.log("finish........")
        self.log(self.url_list.__len__())
        # self.write_to_file()




        return 0

    def parse(self, response):
        partten = '[^/]*/[^/]*$'
        self.log('parse state')
        file_name = 'repo7.txt'
        sites = json.loads(response.body_as_unicode())
        for i in sites['items']:
            url_temp=i['url']
            # print(url_temp)
            # re.match()

            a = re.search(partten, url_temp)
            # print(".........success")
            if a!=None:
                # print(a.group())
                self.url_list.append(a.group())
            else:
                print(url_temp)
                print("error!!!!!!!!!!")
        with open(file_name,'w') as f:
            for u in self.url_list:
                # self.log(u)
                f.writelines(str(u)+'\n')






    def write_to_file(self):

        file_name = 'repo4.txt'
        self.log('here we are')
        self.log(self.url_list.__len__())
        with open(file_name,'w') as f:
            for u in self.url_list:
                self.log(u)
                f.writelines(u+"\n")

    def err(self):

        self.log("zyispg---error")








if __name__ == '__main__':

    l=crawlRepo()
    l.start_requests()




