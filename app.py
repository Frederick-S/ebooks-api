import os
from ebooks.bootstrap import create_app

app = create_app(os.environ.get('FLASK_APP_MODE') or 'development')

if __name__ == '__main__':
    app.run()
