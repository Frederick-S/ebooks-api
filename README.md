# ebooks-api - Search ebooks from various sites.
[![Build Status](https://travis-ci.org/Frederick-S/ebooks-api.svg?branch=master)](https://travis-ci.org/Frederick-S/ebooks-api) [![Build status](https://ci.appveyor.com/api/projects/status/um58744xnjbyihfw/branch/master?svg=true)](https://ci.appveyor.com/project/Frederick-S/ebooks-api/branch/master) [![codecov](https://codecov.io/gh/Frederick-S/ebooks-api/branch/master/graph/badge.svg)](https://codecov.io/gh/Frederick-S/ebooks-api) [![Requirements Status](https://requires.io/github/Frederick-S/ebooks-api/requirements.svg?branch=master)](https://requires.io/github/Frederick-S/ebooks-api/requirements/?branch=master) [![codebeat badge](https://codebeat.co/badges/79464d38-d559-41e1-9f35-85efc6b15ce4)](https://codebeat.co/projects/github-com-frederick-s-ebooks-api-master) [![Maintainability](https://api.codeclimate.com/v1/badges/59306eeaf09e0cd50a6d/maintainability)](https://codeclimate.com/github/Frederick-S/ebooks-api/maintainability)

## API
### Query ebooks
#### HTTP request
```
GET /v1.0/ebooks
```

#### Query parameters
|Name   |Required   |Description   |
|---|---|---|
|provider   |Y   |The ebook provider, one of `weread,duokan,douban,turing,epubit`.   |
|title   |Y   |The title of book.   |
|lastBookIndex   |N   |Only required by `weread`. When this value is set, it queries books whose index is greater than `lastBookIndex`.   |
|pageIndex|N|Required by `duokan,douban,turing,epubit`, When this value is set, it queries books after `pageIndex - 1` pages.|

## License
[MIT](LICENSE)
