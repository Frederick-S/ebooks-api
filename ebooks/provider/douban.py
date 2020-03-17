import requests
from ebooks.provider.ebook import Ebook
from ebooks.provider.ebook_provider import EbookProvider


class DoubanEbookProvider(EbookProvider):
    def __init__(self):
        self.url = 'https://read.douban.com/j/search_v2'

    def get_ebooks(self, title, last_book_index, page_index):
        data = {
            "sort": "default",
            "page": page_index,
            "q": title,
            "query": "query getFilterWorksList($works_ids: [ID!]) {      "
                     "worksList(worksIds: $works_ids) {                "
                     "title    cover    url    isBundle    isOrigin    "
                     "vip {      canRead    }    limitedVip {      canRead"
                     "      isActive    }    promotion {      endTime    }    "
                     "isRebate    fixedPrice    salesPrice          url    "
                     "title          author {      name      url    }    "
                     "origAuthor {      name      url    }    translator "
                     "{      name      url    }          abstract    "
                     "editorHighlight          isOrigin    kinds {          "
                     "name @skip(if: true)    shortName @include(if: true)    "
                     "id      }    ... on WorksBase @include(if: true) {      "
                     "wordCount      wordCountUnit    }    ... on WorksBase "
                     "@include(if: false) {          isEssay        ... on "
                     "EssayWorks {      favorCount    }          isNew        "
                     "averageRating    ratingCount    url          }    ... "
                     "on WorksBase @include(if: false) {      isColumn      "
                     "isEssay      onSaleTime      ... on ColumnWorks {     "
                     "updateTime}    }    ... on WorksBase @include(if: true) "
                     "{      isColumn  ... on ColumnWorks {   isFinished      "
                     "}    }    ... on EssayWorks { essayActivityData {       "
                     "title    uri    tag {      name color      background   "
                     "icon2x      icon3x      iconSize {   height      }      "
                     "iconPosition {        x y      }    }        }    }    "
                     "highlightTags {    name    }      isInLibrary   ... on "
                     "WorksBase @include(if: false) {          fixedPrice    "
                     "salesPrice    isRebate      }    ... on EbookWorks {    "
                     "fixedPrice    salesPrice    isRebate      }    ... on "
                     "WorksBase @include(if: true) {      ... on EbookWorks { "
                     "id        isPurchased        isInWishlist      }    }   "
                     "id        isOrigin      }    }"
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.132 Safari/537.36'
        }
        response = requests.post(self.url, json=data, headers=headers)

        if response.status_code != requests.codes.ok:
            raise Exception(response.text)

        body = response.json()
        books = body.get('list', [])

        return list(map(self.__convert_to_ebook, books))

    def __convert_to_ebook(self, book):
        ebook = Ebook()
        ebook.title = book.get('title', '')
        ebook.author = self.__get_author(book)
        ebook.price = book.get('salesPrice', 0.0) / 100.0
        ebook.cover = book.get('cover', '')
        ebook.intro = book.get('abstract', '')

        return ebook

    def __get_author(self, book):
        authors = book.get('origAuthor') or book.get('author')

        return ' '.join(list(map(lambda x: x.get('name'), authors))) \
            if len(authors) > 0 else ''
