# ebooks-api - Search ebooks from various sites
[![Build Status](https://travis-ci.org/Frederick-S/ebooks-api.svg?branch=master)](https://travis-ci.org/Frederick-S/ebooks-api) [![Build status](https://ci.appveyor.com/api/projects/status/um58744xnjbyihfw/branch/master?svg=true)](https://ci.appveyor.com/project/Frederick-S/ebooks-api/branch/master) [![codecov](https://codecov.io/gh/Frederick-S/ebooks-api/branch/master/graph/badge.svg)](https://codecov.io/gh/Frederick-S/ebooks-api) [![Requirements Status](https://requires.io/github/Frederick-S/ebooks-api/requirements.svg?branch=master)](https://requires.io/github/Frederick-S/ebooks-api/requirements/?branch=master) [![codebeat badge](https://codebeat.co/badges/79464d38-d559-41e1-9f35-85efc6b15ce4)](https://codebeat.co/projects/github-com-frederick-s-ebooks-api-master) [![Maintainability](https://api.codeclimate.com/v1/badges/59306eeaf09e0cd50a6d/maintainability)](https://codeclimate.com/github/Frederick-S/ebooks-api/maintainability)

The server side of [ebooks-web](https://github.com/Frederick-S/ebooks-web).

## API
### Query ebooks
#### HTTP request
```http
GET /v1.0/ebooks
```

#### Query parameters
|Name   |Required   |Description   |
|---|---|---|
|provider   |Y   |The ebook provider, one of `weread,duokan,douban,turing,epubit,kindle`.   |
|title   |Y   |The title of book.   |
|lastBookIndex   |N   |Only required by `weread`. When this value is set, it queries books whose index is greater than `lastBookIndex`.   |
|pageIndex|N|Required by `duokan,douban,turing,epubit,kindle`. When this value is set, it queries books after `pageIndex - 1` pages.|

#### Example
##### Request
```http
GET /v1.0/ebooks?provider=weread&title=python
```

##### Response
```http
HTTP/1.1 200 OK
Content-type: application/json
Content-length: 123

[
    {
        "author": "卢西亚诺·拉马略",
        "cover": "https://rescdn.qqmail.com/weread/cover/910/22806910/s_22806910.jpg",
        "intro": "本书致力于帮助Python开发人员挖掘这门语言及相关程序库的优秀特性，避免重复劳动，同时写出简洁、流畅、易读、易维护，并且具有地道Python风格的代码。本书尤其深入探讨了Python语言的高级用法，涵盖数据结构、Python风格的对象、并行与并发，以及元编程等不同的方面。",
        "price": 69.99,
        "title": "流畅的Python"
    },
    {
        "author": "埃里克·马瑟斯",
        "cover": "https://rescdn.qqmail.com/weread/cover/930/22806930/s_22806930.jpg",
        "intro": "本书是一本针对所有层次的Python读者而作的Python入门书。全书分两部分：第一部分介绍用Python编程所必须了解的基本概念，包括matplotlib、NumPy和Pygal等强大的Python库和工具介绍，以及列表、字典、if语句、类、文件与异常、代码测试等内容；第二部分将理论付诸实践，讲解如何开发三个项目，包括简单的Python2D游戏开发，如何利用数据生成交互式的信息图，以及创建和定制简单的Web应用，并帮读者解决常见编程问题和困惑。本书适合对Python感兴趣的任何层次的读者阅读。",
        "price": 44.5,
        "title": "Python编程：从入门到实践"
    },
    {
        "author": "Mark Lutz 著",
        "cover": "https://rescdn.qqmail.com/weread/cover/792/621792/s_621792.jpg",
        "intro": "",
        "price": 30,
        "title": "Python学习手册（原书第4版）"
    }
]
```

## License
[MIT](LICENSE)
