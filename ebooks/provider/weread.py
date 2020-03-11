import requests
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class WereadEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://weread.qq.com/web/search/global?' \
                   'keyword={}&maxIdx={}&count={}'

    def get_ebooks(self, book_name, last_book_id, page_size):
        url = self.url.format(book_name, last_book_id, page_size)
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        body = response.json()
        books = body.get('books', [])

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        book_info = book.get('bookInfo')
        ebook = Ebook()
        ebook.title = book_info.get('title', '')
        ebook.author = book_info.get('author', '')
        ebook.price = book_info.get('price', 0.0)
        ebook.cover = book_info.get('cover', '')
        ebook.intro = book_info.get('intro', '')

        return ebook
