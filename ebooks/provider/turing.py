import requests
from pyquery import PyQuery
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class TuringEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://www.ituring.com.cn/menu/books?q={}&page={}'

    def get_ebooks(self, book_name, last_book_index, page_index):
        url = self.url.format(book_name, page_index)
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        document = PyQuery(response.text)
        books = [PyQuery(book) for book in document.find('.block-item')]

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        ebook = Ebook()
        ebook.title = book.find('.name').text()
        ebook.author = book.find('.author').text()
        ebook.cover = book.find('.book-img img').attr('src')
        ebook.intro = book.find('.intro').text()

        return ebook
