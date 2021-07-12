from random import getrandbits, randint, randrange
from ipaddress import IPv4Address
from datetime import timedelta, datetime

from src import create_app

app = create_app()

from src import db, User, Post, ViewHistory

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def create_history(db, post, x=1):
    """
    This function will create history objects and store them into the
    database.
    """
    for i in range(0, int(50000/x)):
        hist = ViewHistory()
        hist.ip_address = str(IPv4Address(getrandbits(32)))
        hist.post = post
        hist.created = random_date(datetime(2020, 1, 1), datetime(2020, 6, 1))
        db.session.add(hist)

with app.app_context():

    db.create_all()     # create tables from models

    user1 = User(
        name="Michael Jackson",
        email='tom.jack@gmail.com'
    )

    user2 = User(
        name="Nick Cage",
        email='cageman01@gmail.com'
    )

    user3 = User(
        name="Adam Sandler",
        email='sandyman@aol.com'
    )

    user4 = User(
        name="Arnold Schwarzenegger",
        email='terminator@gmail.com'
    )

    user5 = User(
        name="John Cena",
        email='ucantseeme@live.com'
    )

    post1 = Post()
    post1.title = "Music is awesome"
    post1.body = "Today I performed in front of thousands of people"
    post1.author = user1
    create_history(db, post1, 5)

    post2 = Post()
    post2.title = "You don't say"
    post2.body = "People these days..."
    post2.author = user2
    create_history(db, post2, 4)

    post3 = Post()
    post3.title = "Not happy"
    post3.body = "Just Googled 'meme' and my face came up"
    post3.author = user3
    create_history(db, post3, 3)

    post4 = Post()
    post4.title = "01110010"
    post4.body = "I'll be back"
    post4.author = user4
    create_history(db, post4, 2)

    post5 = Post()
    post5.title = "Stay Strong"
    post5.body = "I just benched 400kg the other day, too easy"
    post5.author = user4
    create_history(db, post5, 1)

    post6 = Post()
    post6.title = "Interesting day"
    post6.body = "Nobody could see me today, strange..."
    post6.author = user5
    create_history(db, post6)

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.commit()

    print(User.query.all())
    print(Post.query.all())

