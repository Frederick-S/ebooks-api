import requests
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class TuringEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://api.ituring.com.cn/api/Search/Advanced'

    def get_ebooks(self, title, last_book_index, page_index):
        data = {
            'categoryId': 0,
            'edition': 4,
            'name': title,
            'page': page_index
        }
        response = requests.post(self.url, json=data)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        body = response.json()

        return list(map(self.__convert_to_ebook, body.get('bookItems', {})))

    def __convert_to_ebook(self, book):
        ebook = Ebook()
        ebook.title = book.get('name', '')
        ebook.author = book.get('authorNameString', '')
        ebook.price = self.__get_price(book.get('bookEditionPrices', []))
        ebook.cover = 'https://file.ituring.com.cn/LargeCover/{}'.format(book.get('coverKey', ''))
        ebook.intro = book.get('abstract', '')

        return ebook

    def __get_price(self, prices):
        for price in prices:
            if price.get('key', '') == 'Ebook':
                return price.get('name', '')

        return 0.0
