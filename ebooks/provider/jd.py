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

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        image = book.find('.p-img img')
        ebook = Ebook()
        ebook.title = book.find('.p-name').text()
        ebook.author = book.find('.p-bi-name a[title]').text()
        ebook.cover = image.attr('src') or image.attr('data-lazy-img')

        return ebook
