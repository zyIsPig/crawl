import scrapy
import json
from myfirstSpider.spiders.url_constructor import github_search_url
import time
from myfirstSpider.spiders.header_constructor import header_construct
import re
from myfirstSpider.spiders.q_constructor import q
from myfirstSpider.spiders.util import read_to_list
import os
from myfirstSpider.spiders.util import *
class crawlRepo(scrapy.Spider):


    name = 'repo_pull'
    cnt=0
    url_list = []
    def __init__(self):
        self.url_list=[]


    def start_requests(self):
        self.url_list=read_to_list('/Users/gulu/myfirstSpider/repo6.txt',14,30
                                   )
        self.cnt=0
        urls=[]
        sta_page=1
        end_page=1
        for url in self.url_list:
            print('finish a repo')
            q1 = q(types=2, repo=url)
            q_str=q1.generate_q()
            print(q_str)
            sta_page=1
            while sta_page<=end_page:

                test1 = github_search_url(q=q_str,type='issues')
                aaa = test1.construct()
            # print(aaa)
                urls.append(aaa)

                head_temp=header_construct(1)


                for url in urls:

                    print(url)

                    yield scrapy.Request(url=url,headers=head_temp,callback=self.parse)


                sta_page+=1

                # time.sleep(1)



            # time.sleep(3)



        self.log("finish........")
        self.log(self.url_list.__len__())
        # self.write_to_file()




        return 0

    def parse(self, response):
        pattern1='[^/]*(?=\+is\%3Apr)'

        self.log('parse state')
        dir_add='/Users/gulu/Desktop/Data1/'
        file_name = re.search(pattern1,response.url).group()

        dir_total=dir_add+file_name
        if not os.path.exists(dir_total):
            os.makedirs(dir_total)
            self.cnt += 1
            print(dir_total)
            # print(response.body)
            print(dir_total+'/'+file_name+'.txt')
            with open(dir_total + '/'+file_name + '.txt', 'wb') as f:

                f.write(response.body)













if __name__ == '__main__':
    url_list = read_to_list('/Users/gulu/myfirstSpider/repo6.txt')

    dir_add = '/Users/gulu/Desktop/Data1/'
    file_name = url_list[1]

    a,b=phase_dir(file_name)
    addr=dir_add+b
    if not os.path.exists(addr):
        os.makedirs(addr)



    print(file_name)

    with open(addr+'/' + '.txt', 'w') as f:

        f.write('zyispig')





