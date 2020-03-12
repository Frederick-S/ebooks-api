import requests
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class EpubitEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://pubcloud.ptpress.cn/pubcloud/operation/front/' \
                   'portal/search?keyword={}&page={}&type=ubook&row=20'

    def get_ebooks(self, book_name, last_book_index, page_index):
        url = self.url.format(book_name, page_index)
        headers = {'Origin-Domain': 'www.epubit.com'}
        response = requests.get(url, headers=headers)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        body = response.json()

        if not body.get('success'):
            raise Exception(body.get('msg'))

        data = body.get('data', {})
        books = data.get('records', [])

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        ebook = Ebook()
        ebook.title = book.get('name', '')
        ebook.price = book.get('price', 0.0)
        ebook.cover = book.get('cover', '')

        return ebook
