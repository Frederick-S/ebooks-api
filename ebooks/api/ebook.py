from flask import jsonify, request
from ebooks.api.api_blueprint import api_blueprint
from ebooks.provider.ebook_provider_factory import EbookProviderFactory


@api_blueprint.route('/ebooks', methods=['GET'])
def get_ebooks():
    provider = request.args.get('provider')
    book_name = request.args.get('bookName')
    last_book_index = request.args.get('lastBookIndex') or 0
    page_index = request.args.get('pageIndex') or 1
    ebook_provider = EbookProviderFactory.create(provider)

    if not ebook_provider:
        return 'Invalid ebook provider', 400

    if not book_name:
        return 'Missing bookName', 400

    ebooks = ebook_provider.get_ebooks(
        book_name, last_book_index, page_index)

    return jsonify([ebook.serialize() for ebook in ebooks])
