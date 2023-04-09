from flask import Flask

from config.commands import register_commands
from config.db import configure_db
from config.settings import SECRET_KEY, db


def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        configure_db(app, db)
        register_commands(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8005)
