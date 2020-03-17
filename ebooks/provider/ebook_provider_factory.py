from ebooks.provider.douban import DoubanEbookProvider
from ebooks.provider.duokan import DuokanEbookProvider
from ebooks.provider.epubit import EpubitEbookProvider
from ebooks.provider.kindle import KindleEbookProvider
from ebooks.provider.turing import TuringEbookProvider
from ebooks.provider.weread import WereadEbookProvider


class EbookProviderFactory:
    providers = {
        'weread': WereadEbookProvider(),
        'duokan': DuokanEbookProvider(),
        'turing': TuringEbookProvider(),
        'epubit': EpubitEbookProvider(),
        'douban': DoubanEbookProvider(),
        'kindle': KindleEbookProvider()
    }

    @staticmethod
    def create(provider):
        return EbookProviderFactory.providers.get(provider, None)
