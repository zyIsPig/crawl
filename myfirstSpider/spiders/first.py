import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://api.github.com/users/Zyispig"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        filename = 'zyispig.html'
        with open(filename, 'wb') as f:
            f.writelines(response)
        self.log('Saved file %s' % filename)
