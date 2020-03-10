from ebooks.api.api_blueprint import api_blueprint


@api_blueprint.route('/ebooks', methods=['GET'])
def get_ebooks():
    return 'hello'
