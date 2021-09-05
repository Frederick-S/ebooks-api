import requests
from pyquery import PyQuery
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class JDEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://s-e.jd.com/Search?key={}&page={}&enc=utf-8'

    def get_ebooks(self, title, last_book_index, page_index):
        url = self.url.format(title, page_index)
        response = requests.get(url)
        response.encoding = 'utf-8'

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        document = PyQuery(response.text)
        books = [PyQuery(book) for book in
                 document.find('.goods-list-ebook li')]
        sku_ids = list(map(self.__get_sku_id, books))
        prices = self.__get_prices(sku_ids)

        return list(map(
            lambda book: self.__convert_to_ebook(book, prices), books))

    def __convert_to_ebook(self, book, prices):
        sku_id = self.__get_sku_id(book)
        image = book.find('.p-img img')

        ebook = Ebook()
        ebook.title = book.find('.p-name').text()
        ebook.author = book.find('.p-bi-name a[title]').text()
        ebook.price = prices.get(sku_id, 0.0)
        ebook.cover = image.attr('src') or image.attr('data-lazy-img')

        return ebook

    def __get_sku_id(self, book):
        return 'J_' + book.attr('data-sku')

    def __get_prices(self, sku_ids):
        if not sku_ids:
            return []

        url = 'https://p.3.cn/prices/mgets?skuIds={}'.format(','.join(sku_ids))
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; '
                          'Intel Mac OS X 10.15; rv:91.0) '
                          'Gecko/20100101 Firefox/91.0'
        })
        data = response.json()

        return {x.get('id'): float(x.get('p')) for x in data}
