from flask import request
from . import controllers


def init(app):
    @app.route('/')
    def index():
        return controllers.get_index()

    @app.route('/cards/create')
    def create_card_page():
        return controllers.get_create_card()

    @app.route('/cards', methods=['post'])
    def create_card():
        front = request.form['front']
        back = request.form['back']
        return controllers.post_create_card(front, back)

    @app.route('/cards', methods=['get'])
    def read_all_cards_page():
        return controllers.get_all_cards()

    @app.errorhandler(404)
    def page_not_found(error):
        return controllers.page_not_found()
