from flask import render_template, redirect, url_for
from . import db


def get_index():
    card = db.read_random_card()
    return render_template('index.html', card=card)


def get_create_card():
    return render_template('create-card.html')


def post_create_card(front, back):
    reject_reasons = []
    if front == '':
        reject_reasons.append('Front is not present.')
    if back == '':
        reject_reasons.append('Back is not present.')

    if len(reject_reasons) > 0:
        return render_template('400.html', reasons=reject_reasons), 400

    success = db.create_card(front, back)
    if not success:
        return render_template('500.html'), 500

    return redirect(url_for('index'))


def get_all_cards():
    cards = db.read_all_cards()
    return render_template('read-all-cards.html', cards=cards)


def page_not_found():
    return render_template('404.html'), 404
