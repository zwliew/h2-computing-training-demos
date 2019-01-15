from flask import Flask


def create():
    from . import routes, db
    app = Flask(__name__)
    routes.init(app)
    db.init()
    return app


app = create()
