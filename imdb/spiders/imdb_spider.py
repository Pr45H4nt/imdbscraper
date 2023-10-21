import scrapy
import re

class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"
    headers = {
    "authority": "www.imdb.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US,en;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Brave\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
    

    def start_requests(self):
        url = "https://www.imdb.com/search/title/?title_type=movie&genres=sci-fi&explore=genres"
        yield scrapy.Request(
            url = url ,
            headers= self.headers
        )

    def parse(self, response):
        links = response.xpath('//h3[@class="lister-item-header"]/a/@href').getall()
        for link in links:
            yield scrapy.Request(
                url = 'https://www.imdb.com' + link,
                callback= self.parse_details,
                headers = self.headers
            )
        next_btn = response.xpath('//a[@class="lister-page-next next-page"]/@href').get()
        if next_btn:
            yield scrapy.Request(
                url = 'https://www.imdb.com' + next_btn,
                callback= self.parse,
                headers = self.headers
            )

    def parse_details(self,response):
        s = response.xpath('//meta[@property="og:title"]/@content').get()

        # Extract name
        name = re.search(r"^(.*)\(\d{4}\)", s).group(1).strip()

        # Extract date (year)
        date = int(re.search(r"\((\d{4})\)", s).group(1))

        # Extract rating
        try:
            rating = float(re.search(r"⭐ (\d+\.\d+)", s).group(1))
        except:
            rating = None

        # Extract genres
        genres = re.search(r"\| (.+)$", s).group(1).split(', ')

        s2 = (response.xpath('//meta[@property="og:description"]/@content').get()).split('|')
        time_duration = s2[0]
        try:
            age_group = s2[1]
        except:
            age_group = None

        directors = list(set(response.xpath('//li[@data-testid = "title-pc-principal-credit"][contains(., "Director")]//li[@role="presentation"]//text()').getall()))
        writers = list(set(response.xpath('//li[@data-testid = "title-pc-principal-credit"][contains(., "Writers")]//li[@role="presentation"]//text()').getall()))
        stars = list(set(response.xpath('//li[@data-testid = "title-pc-principal-credit"][contains(., "Stars")]//li[@role="presentation"]//text()').getall()))
        
        data_dict = {
            'Title' : name , 
            'Released Year' : date ,
            'Rating' : rating , 
            'Genres' : genres ,
            'Length' : time_duration ,
            'Certification' : age_group ,
            'Directors' : directors,
            'Writers' : writers ,
            'Stars' : stars
        }
        
        yield data_dict