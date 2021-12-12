import requests
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class DuokanEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://www.duokan.com/target/search/web/{}/{}'

    def get_ebooks(self, title, last_book_index, page_index):
        url = self.url.format(title, page_index)
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        data = response.json()

        return list(map(self.__convert_to_ebook, data.get('books', [])))

    def __convert_to_ebook(self, book):
        ebook = Ebook()
        ebook.title = book.get('title', '')
        ebook.author = book.get('authors', '')
        ebook.price = book.get('price', '')
        ebook.cover = book.get('cover', '')
        ebook.abstract = book.get('summary', '')

        return ebook
