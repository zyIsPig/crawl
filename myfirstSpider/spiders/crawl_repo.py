import scrapy

from myfirstSpider.spiders.url_constructor import github_search_url


class crawlRepo(scrapy.Spider):

    name='repo_crawler'


    def start_requests(self):
        urls=[]
        test1 = github_search_url(q='library', language='java', sort='stars')
        aaa = test1.construct()
        print(aaa)
        urls.append(aaa)
        for url in urls:
            print('...........')
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)

        return 0

    def parse(self, response):

        file_name='test2.json'
        with open(file_name,'wb') as f:
            f.write(response.body)

        # self.log('save as %s',file_name)






if __name__ == '__main__':

    test1=github_search_url(q='library',language='java',sort='stars')
    aaa=test1.construct()
    print(aaa)




