import requests
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class DuokanEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://www.duokan.com/target/search/web?s={}&p={}'

    def get_ebooks(self, title, last_book_index, page_index):
        url = self.url.format(title, page_index)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.132 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

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
