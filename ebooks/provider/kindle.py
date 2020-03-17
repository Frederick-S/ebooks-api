import requests
from fake_useragent import UserAgent
from pyquery import PyQuery
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class KindleEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://www.amazon.cn/s?k={}&i=digital-text&page={}'

    def get_ebooks(self, title, last_book_index, page_index):
        headers = {
            'User-Agent': UserAgent(cache=False).random
        }
        url = self.url.format(title, page_index)
        response = requests.get(url, headers=headers)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        document = PyQuery(response.text)
        rows = document.find('div.s-result-list div[data-asin]')
        books = [PyQuery(book) for book in rows]

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        row = PyQuery(book.find('div.sg-row')[1])
        image_wrap = PyQuery(row.children()[0])
        info_wrap = PyQuery(row.children()[1]).find('.sg-row')
        title_author_wrap = PyQuery(info_wrap[0])
        price_wrap = PyQuery(info_wrap[1])
        price = price_wrap.find('.a-price-whole').text() + \
            price_wrap.find('.a-price-fraction').text()

        ebook = Ebook()
        ebook.title = title_author_wrap.find('h2').text()
        ebook.author = title_author_wrap.find('h2')\
            .next().text().split('|')[0].strip()
        ebook.price = book.find('.u-price em').text()
        ebook.cover = image_wrap\
            .find('[data-component-type="s-product-image"] img')\
            .attr('src')
        ebook.price = float(price)

        return ebook
