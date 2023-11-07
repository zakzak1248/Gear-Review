import scrapy

import time


class QuotesSpider(scrapy.Spider):
    name = "boutique"
    base_url="https://www.pluginboutique.com/"
    waiter = 0
    start_urls = [

        # synth
        # "https://www.pluginboutique.com/categories/4-Synth",
        # "https://www.pluginboutique.com/categories/4-Synth?page=0",
        # "https://www.pluginboutique.com/categories/4-Synth?page=1",
        # "https://www.pluginboutique.com/categories/4-Synth?page=2",
        # "https://www.pluginboutique.com/categories/4-Synth?page=3",
        # "https://www.pluginboutique.com/categories/4-Synth?page=4",
        # "https://www.pluginboutique.com/categories/4-Synth?page=5",
        # "https://www.pluginboutique.com/categories/4-Synth?page=6",
        # "https://www.pluginboutique.com/categories/4-Synth?page=7",
        # "https://www.pluginboutique.com/categories/4-Synth?page=8",
        # "https://www.pluginboutique.com/categories/4-Synth?page=9",
        # "https://www.pluginboutique.com/categories/4-Synth?page=10",
        # "https://www.pluginboutique.com/categories/4-Synth?page=11",
        # "https://www.pluginboutique.com/categories/4-Synth?page=12",
        # "https://www.pluginboutique.com/categories/4-Synth?page=13",
        # "https://www.pluginboutique.com/categories/4-Synth?page=14",
        # "https://www.pluginboutique.com/categories/4-Synth?page=15",
        # "https://www.pluginboutique.com/categories/4-Synth?page=16",
        # "https://www.pluginboutique.com/categories/4-Synth?page=17",
        # "https://www.pluginboutique.com/categories/4-Synth?page=18",
        # "https://www.pluginboutique.com/categories/4-Synth?page=19",
        # "https://www.pluginboutique.com/categories/4-Synth?page=20",
        # "https://www.pluginboutique.com/categories/4-Synth?page=21",
        # "https://www.pluginboutique.com/categories/4-Synth?page=22",
        # "https://www.pluginboutique.com/categories/4-Synth?page=23",
        # "https://www.pluginboutique.com/categories/4-Synth?page=24",
        # "https://www.pluginboutique.com/categories/4-Synth?page=25",
        # "https://www.pluginboutique.com/categories/4-Synth?page=26",
        # "https://www.pluginboutique.com/categories/4-Synth?page=27",
        # "https://www.pluginboutique.com/categories/4-Synth?page=28",
        # "https://www.pluginboutique.com/categories/4-Synth?page=29",
        # "https://www.pluginboutique.com/categories/4-Synth?page=30",
        # "https://www.pluginboutique.com/categories/4-Synth?page=31",
        # "https://www.pluginboutique.com/categories/4-Synth?page=32",
        # "https://www.pluginboutique.com/categories/4-Synth?page=33",
        # "https://www.pluginboutique.com/categories/4-Synth?page=34",
        # "https://www.pluginboutique.com/categories/4-Synth?page=35",
        # "https://www.pluginboutique.com/categories/4-Synth?page=36",
        # "https://www.pluginboutique.com/categories/4-Synth?page=37",
        # "https://www.pluginboutique.com/categories/4-Synth?page=38",
        # "https://www.pluginboutique.com/categories/4-Synth?page=39",
        # "https://www.pluginboutique.com/categories/4-Synth?page=40",
        # "https://www.pluginboutique.com/categories/4-Synth?page=51",
        # "https://www.pluginboutique.com/categories/4-Synth?page=52",
        # "https://www.pluginboutique.com/categories/4-Synth?page=53",
        # "https://www.pluginboutique.com/categories/4-Synth?page=54",
        # "https://www.pluginboutique.com/categories/4-Synth?page=55",
        # "https://www.pluginboutique.com/categories/4-Synth?page=56",
        # "https://www.pluginboutique.com/categories/4-Synth?page=57",
        # "https://www.pluginboutique.com/categories/4-Synth?page=58",
        # "https://www.pluginboutique.com/categories/4-Synth?page=59",
        # "https://www.pluginboutique.com/categories/4-Synth?page=60",
        # "https://www.pluginboutique.com/categories/4-Synth?page=61",
        # "https://www.pluginboutique.com/categories/4-Synth?page=62",
        # "https://www.pluginboutique.com/categories/4-Synth?page=63",
        # "https://www.pluginboutique.com/categories/4-Synth?page=64",
        # "https://www.pluginboutique.com/categories/4-Synth?page=65",
        # "https://www.pluginboutique.com/categories/4-Synth?page=66",
        # "https://www.pluginboutique.com/categories/4-Synth?page=67",
        # "https://www.pluginboutique.com/categories/4-Synth?page=68",
        # "https://www.pluginboutique.com/categories/4-Synth?page=69",
        # "https://www.pluginboutique.com/categories/4-Synth?page=70",
        # "https://www.pluginboutique.com/categories/4-Synth?page=71",
        # "https://www.pluginboutique.com/categories/4-Synth?page=72",
        # "https://www.pluginboutique.com/categories/4-Synth?page=73",
        # "https://www.pluginboutique.com/categories/4-Synth?page=74",
        # "https://www.pluginboutique.com/categories/4-Synth?page=75",
        # "https://www.pluginboutique.com/categories/4-Synth?page=76",
        # "https://www.pluginboutique.com/categories/4-Synth?page=77",
        # "https://www.pluginboutique.com/categories/4-Synth?page=78",
        # "https://www.pluginboutique.com/categories/4-Synth?page=79",

    ]


    def parse(self, response):
        # page view
        # products >>> response.css(".producttile")
        # product title >>> response.css(".producttile")[X].css("a")[0].attrib['title']
        # product brand >>> response.css(".producttile")[X].css(".producttile-meta")[0].xpath("a")[1].attrib['title']
        # product URL   >>> response.css(".producttile")[X].css("a")[0].attrib['href']
        for product in response.css(".producttile"):
            # print("aint scared of no ghost")
            product_url= product.css("a")[0].attrib['href']
            # print(product_url)
            yield scrapy.Request(
                response.urljoin(self.base_url+"/" + product_url),
                callback=self.parse_product,
                meta={
                    "title": product.css("a")[0].attrib['title'],
                    "brand": product.css(".producttile-meta")[0].xpath("a")[1].attrib['title'],
                    "url":   product.css("a")[0].attrib['href']})
            time.sleep(.05 + self.waiter)
            self.waiter+=1
            if self.waiter>30: self.waiter=0
            # return

    def parse_product(self, response):
        import json
        # print(response.status,'\n',response.url)
        rating_data = response.css('div[data-react-class="RatingInfoDetails"]')
        description = response.xpath("//div[@itemprop='description']").get()
        if(description == None):
            description = response.xpath("/html/body/div[3]/div[2]/div[5]/div[4]/div[4]").get()

        # rating_overall = json.loads(rating_data[0].attrib['data-react-props'])['rating']['overall']
        rating_overall = ""

        rating_data_str = response.css('div[data-react-class="RatingInfoDetails"]').attrib.get('data-react-props', '{}')

        try:
            # Load the JSON string into a dictionary
            rating_data = json.loads(rating_data_str)
            # Extract the overall rating from the loaded JSON data
            rating_overall = rating_data.get('rating', {}).get('overall')
        except:
            # Handle JSON decoding error (e.g., if the 'data-react-props' attribute is not valid JSON)
            rating_overall =""

        title = response.meta['title']
        brand = response.meta['brand']
        url = response.meta['url']
        yield {"title": title,
                "brand": brand,
                "url": url,
                "rating": rating_overall,
                "description": description
                }




