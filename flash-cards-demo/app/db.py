import sqlite3
import os


def get():
    db = sqlite3.connect('db.sqlite3')
    db.row_factory = sqlite3.Row
    return db


def create():
    db = get()
    db.execute('create table card (front TEXT, back TEXT)')
    db.close()


def seed():
    db = get()
    data = [
        ('How many days does it take for the Earth to orbit the Sun?', '365'),
        ('How much wood would a woodchuck chuck if a woodchuck could chuck wood?', '700 pounds'),
        ('Does cold water freeze quicker than hot water?', 'Great question! In fact, this topic has been of much debate over the course of several decades, with observations of the phenomena dating back to Artistotle\'s time (~300 BC!). Scientists nowadays call it the \'Mpemba Effect\' (The M is NOT silent!). Till today, there is no concrete evidence as to when, how, and why the phenonemon actually occurs. So, the answer to this question is TBD.'),
        ('According to the lyrics of the hit Queen song Killer Queen, where did perfume naturally come from?', 'Paris'),
        ('Tasmania is an isolated island state belonging to which country?', 'Australia'),
        ('How many electrons does a hydrogen atom have?', '1')
    ]
    with db:
        db.executemany('insert into card values (?,?)', data)
    db.close()


def init():
    if not os.path.isfile('db.sqlite3'):
        create()
        seed()


def read_card(id):
    db = get()
    card = db.execute(
        'select * from card, where rowid=?', (id)).fetchone()
    db.close()
    return card


def read_random_card():
    db = get()
    card = db.execute(
        'select * from card where rowid in (select rowid from card order by random() limit 1)').fetchone()
    db.close()
    return card


def read_all_cards():
    db = get()
    cards = db.execute('select rowid, * from card').fetchall()
    db.close()
    return cards


# Returns True on success, False otherwise
def create_card(front, back):
    db = get()
    try:
        with db:
            db.execute('insert into card(front, back) values (?,?)',
                       (front, back))
    except sqlite3.Error:
        return False
    db.close()
    return True
