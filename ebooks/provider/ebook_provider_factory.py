from ebooks.provider.duokan import DuokanEbookProvider
from ebooks.provider.weread import WereadEbookProvider


class EbookProviderFactory:
    providers = {
        'weread': WereadEbookProvider(),
        'duokan': DuokanEbookProvider()
    }

    @staticmethod
    def create(provider):
        return EbookProviderFactory.providers.get(provider, None)
