from ebooks.provider.weread import WereadEbookProvider


class EbookProviderFactory:
    providers = {
        'weread': WereadEbookProvider()
    }

    @staticmethod
    def create(provider):
        return EbookProviderFactory.providers.get(provider, None)
