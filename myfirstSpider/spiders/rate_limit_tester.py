import scrapy
from myfirstSpider.spiders.header_constructor import header_construct


# rate_limit_url: https://api.github.com/rate_limit
class rate_tester(scrapy.Spider):

    name='rate_limit'


    def start_requests(self):
        head_test = header_construct(1)
        urls = [
            "https://api.github.com/rate_limit"
        ]
        for url in urls:
            yield scrapy.Request(url=url,headers=head_test, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # log_file='rate_limit.txt'
        # with open(log_file,'wb') as f:
        #     f.write(response.body())
        print("zyispig")
        print(response.body)
