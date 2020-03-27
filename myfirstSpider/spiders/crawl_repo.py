import scrapy

import json
from myfirstSpider.spiders.url_constructor import github_search_url


class crawlRepo(scrapy.Spider):

    name='repo_crawler'


    def start_requests(self):
        urls=[]


        test1 = github_search_url(q='library', language='java', sort='stars',page=2,per_page=100)
        aaa = test1.construct()
        print(aaa)
        urls.append(aaa)
        for url in urls:
            print('...........')
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)

        return 0

    def parse(self, response):
        url_list=[]
        file_name='repo.txt'
        sites = json.loads(response.body_as_unicode())
        for i in sites['items']:
            url_temp=i['url']
            print(".........")
            print(url_temp)
            url_list.append(url_temp)
        # with open(file_name,'wb') as f:
        #
        #
        #
        #     f.write(response.body)

        # self.log('save as %s',file_name)

        with open(file_name,'w') as f:
            for u in url_list:
                f.writelines(u+"\n")








if __name__ == '__main__':

    test1=github_search_url(q='library',language='java',sort='stars')
    aaa=test1.construct()
    print(aaa)




