from flask import jsonify, request
from ebooks.api.api_blueprint import api_blueprint
from ebooks.provider.ebook_provider_factory import EbookProviderFactory


@api_blueprint.route('/ebooks', methods=['GET'])
def get_ebooks():
    provider = request.args.get('provider')
    book_name = request.args.get('book_name')
    last_book_id = request.args.get('last_book_id') or 0
    page_size = request.args.get('page_size') or 20
    ebook_provider = EbookProviderFactory.create(provider)

    if not ebook_provider:
        return 'Invalid ebook provider', 400

    if not book_name:
        return 'Missing book_name', 400

    ebooks = ebook_provider.get_ebooks(book_name, last_book_id, page_size)

    return jsonify([ebook.serialize() for ebook in ebooks])
