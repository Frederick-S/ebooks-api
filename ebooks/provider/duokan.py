import requests
from pyquery import PyQuery
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class DuokanEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://www.duokan.com/search/{}/{}'

    def get_ebooks(self, title, last_book_index, page_index):
        url = self.url.format(title, page_index)
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        document = PyQuery(response.text)
        books = [PyQuery(book) for book in document.find('.u-list li')]

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        ebook = Ebook()
        ebook.title = book.find('.title').text()
        ebook.author = book.find('.u-author').text()
        ebook.price = float(
            book.find('.u-price em').text().replace('¥', '').strip())
        ebook.cover = book.find('.cover img').attr('src')
        ebook.intro = book.find('.desc').text()

        return ebook
