import scrapy

class JobsSpider(scrapy.Spider):
    name = "gradcracker"
    start_urls = ["https://www.gradcracker.com/search/computing-technology-graduate-jobs?page=1",]

    def parse(self, response):
        for resultCard in response.css("div.job-item"):
            yield   {
                "url"      : resultCard.css("h2 a::attr(href)").extract_first(),
                "company"  : resultCard.css("h2 a::attr(href)").extract_first().split("/")[5],
                "jobTitle" : str(resultCard.css("h2 a::text").extract_first()).strip(),
                "location" : str(resultCard.css("div.item:nth-child(2)::text").extract()[1]).strip(),
                "salary"   : str(resultCard.css("div.item:nth-child(1)::text").extract()[1]).strip(),
            }

            nextPage = response.css("div.text-center li a[rel=next]::attr(href)").extract_first()
            if nextPage is not None:
                yield response.follow(nextPage, callback=self.parse)

            # yield {
            #     "url" : resultCard.xpath("/html/body/div[2]/div[3]/div/div[2]/div[18]/div[2]/h2/a/@href").extract_first(),
            #     "company": resultCard.xpath("/html/body/div[2]/div[3]/div/div[2]/div[18]/div[2]/h2/a/@href").extract_first().split("/")[5],
            #     "jobTitle": resultCard.xpath("/html/body/div[2]/div[3]/div/div[2]/div[3]/div[2]/h2/a/text()").extract_first(),
            #     "location": resultCard.xpath("/html/body/div[2]/div[3]/div/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/text()").extract()[1],
            #     "salary": resultCard.xpath("/html/body/div[2]/div[3]/div/div[2]/div[3]/div[2]/div[3]/div[1]/div[1]/text()").extract()[1]
            # }

            # yield {
            #     "url": resultCard.css("h2 a::attr(href)").extract_first(),
            #     "company": resultCard.css("h2 a::attr(href)").extract_first().split("/")[5],
            #     "jobTitle": str(resultCard.css("h2 a::text").extract_first()).strip(),
            #     "location": str(resultCard.css("div.item:nth-child(2)::text").extract()[1]).strip(),
            #     "salary": str(resultCard.css("div.item:nth-child(1)::text").extract()[1]).strip(),
            # }