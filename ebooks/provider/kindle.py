import requests
from pyquery import PyQuery
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class KindleEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://www.amazon.cn/s?k={}&i=digital-text&page={}'

    def get_ebooks(self, title, last_book_index, page_index):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.132 Safari/537.36'
        }
        url = self.url.format(title, page_index)
        response = requests.get(url, headers=headers)
        blocked = 'api-services-support@amazon.com' in response.text

        if response.status_code != requests.codes.ok:
            raise Exception('Blocked by Amazon' if blocked else response.text)

        if blocked:
            raise Exception('Blocked by Amazon')

        document = PyQuery(response.text)
        rows = document.find(
            'div.s-result-item[data-asin]:not([data-asin=""])')
        books = [PyQuery(book) for book in rows]

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        row = PyQuery(book.find('div.sg-row')[1])
        info_wrap = PyQuery(row.children()[1])
        sections = info_wrap.find('div.a-section div.a-section')
        title_author_wrap = PyQuery(sections[0])
        price_wrap = PyQuery(sections[2])
        price = price_wrap.find('.a-price-whole').text() + \
            price_wrap.find('.a-price-fraction').text()

        ebook = Ebook()
        ebook.title = title_author_wrap.find('h2').text()
        ebook.author = title_author_wrap.find('h2')\
            .next().text().split('|')[0].strip()
        ebook.price = book.find('.u-price em').text()
        ebook.cover = book.find('span[data-component-type="s-product-image"]')\
            .find('img').attr('src')
        ebook.price = float(price) if price != '' else 0

        return ebook
