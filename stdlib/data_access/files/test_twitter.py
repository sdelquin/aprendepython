import sqlite3
from pathlib import Path
from typing import Generator

import pytest
from twitter import Tweet, Twitter, TwitterError, User, create_db

TEST_DB_PATH = 'test_twitter.db'


# **************************************************************
# FIXTURES
# **************************************************************


@pytest.fixture(autouse=True)
def create_test_database():
    try:
        create_db(TEST_DB_PATH)
        yield
    except Exception as err:
        raise err
    finally:
        Path(TEST_DB_PATH).unlink(missing_ok=True)


@pytest.fixture
def db_con():
    con = sqlite3.connect(TEST_DB_PATH)
    con.row_factory = sqlite3.Row
    yield con
    con.close()


@pytest.fixture(autouse=True)
def make_dbutils_use_test_database(monkeypatch: pytest.MonkeyPatch):
    sconnect = sqlite3.connect

    def mock_sqlite3_connect(*args, **kwargs):
        return sconnect(TEST_DB_PATH)

    monkeypatch.setattr(sqlite3, 'connect', mock_sqlite3_connect)


USER1_PASSWORD = '=1234abcd!'


@pytest.fixture
def user1():
    return User('midudev', USER1_PASSWORD, 'Frontend developer')


USER2_PASSWORD = '@4321dcba*'


@pytest.fixture
def user2():
    return User('mouredev', USER2_PASSWORD, 'Backend developer')


@pytest.fixture
def tweet1():
    return Tweet('This is just fine')


@pytest.fixture
def tweet2():
    return Tweet(retweet_from=1)


@pytest.fixture
def twitter():
    return Twitter()


# **************************************************************
# TESTS
# **************************************************************


def test_create_db(db_con: sqlite3.Connection):
    db_cur = db_con.cursor()

    sql = 'SELECT id, username, password, bio FROM user'
    result = db_cur.execute(sql)
    assert len(result.fetchall()) == 0

    sql = 'SELECT id, content, user_id, retweet_from FROM tweet'
    result = db_cur.execute(sql)
    assert len(result.fetchall()) == 0


def test_build_user(user1: User):
    assert isinstance(user1.con, sqlite3.Connection)
    assert user1.con.row_factory == sqlite3.Row
    assert isinstance(user1.cur, sqlite3.Cursor)

    assert user1.username == 'midudev'
    assert user1.password == USER1_PASSWORD
    assert user1.bio == 'Frontend developer'
    assert user1.id == 0

    u = User('a', 'b')
    assert u.username == 'a'
    assert u.password == 'b'
    assert u.bio == ''
    assert u.id == 0

    u = User('a', 'b', 'c')
    assert u.username == 'a'
    assert u.password == 'b'
    assert u.bio == 'c'
    assert u.id == 0

    u = User('a', 'b', 'c', 99)
    assert u.username == 'a'
    assert u.password == 'b'
    assert u.bio == 'c'
    assert u.id == 99


def test_save_user(user1: User, db_con: sqlite3.Connection):
    user1.save()
    db_cur = db_con.cursor()
    sql = 'SELECT * FROM user WHERE username=?'
    result = db_cur.execute(sql, ('midudev',))
    row = result.fetchone()
    assert row['username'] == user1.username
    assert row['password'] == user1.password
    assert row['bio'] == user1.bio
    assert row['id'] == user1.id
    assert row['id'] > 0


def test_login(user1: User):
    user1.save()

    user1.login(USER1_PASSWORD)
    assert user1.logged is True

    user1.login('5678')
    assert user1.logged is False


def test_tweet(user1: User, db_con: sqlite3.Connection):
    user1.save()
    user1.login(USER1_PASSWORD)
    content = 'Python is cool!'
    tweet = user1.tweet(content)
    assert isinstance(tweet, Tweet)

    db_cur = db_con.cursor()
    sql = 'SELECT * FROM tweet WHERE id=?'
    result = db_cur.execute(sql, (tweet.id,))
    row = result.fetchone()
    assert row['id'] == tweet.id
    assert row['content'] == tweet.content
    assert row['user_id'] == user1.id
    assert row['retweet_from'] == 0


def test_tweet_fails_when_user_is_not_logged(user1: User):
    user1.save()
    with pytest.raises(TwitterError) as err:
        user1.tweet('Error is coming')
    assert str(err.value) == 'User midudev is not logged in!'


def test_tweet_fails_when_user_fails_login(user1: User):
    user1.save()
    user1.login('5678')
    with pytest.raises(TwitterError) as err:
        user1.tweet('Error is coming')
    assert str(err.value) == 'User midudev is not logged in!'


def test_tweet_fails_when_length_is_over_max(user1: User):
    user1.save()
    user1.login(USER1_PASSWORD)
    with pytest.raises(TwitterError) as err:
        user1.tweet(
            """
Elit nisi in tempor dolor Lorem laborum nisi enim sit id duis esse Lorem.
Ut non fugiat excepteur laboris elit consectetur. Voluptate pariatur
ullamco incididunt minim. In exercitation anim eiusmod esse cillum
fugiat fugiat. Fugiat ut fugiat ipsum mollit esse eiusmod. Sunt aute
eiusmod voluptate laborum ipsum duis."""
        )
    assert str(err.value) == 'Tweet has more than 280 chars!'


def test_retweet(user1: User, db_con: sqlite3.Connection):
    user1.save()
    user1.login(USER1_PASSWORD)

    content = 'Think big'

    db_cur = db_con.cursor()
    sql = 'INSERT INTO tweet (content, user_id, retweet_from) VALUES (?, ?, ?)'
    params = (content, user1.id, 0)
    db_cur.execute(sql, params)
    db_con.commit()
    tweet_id = db_cur.lastrowid

    tweet = user1.retweet(tweet_id)
    assert isinstance(tweet, Tweet)

    sql = 'SELECT * FROM tweet WHERE id=?'
    result = db_cur.execute(sql, (tweet.id,))
    row = result.fetchone()
    assert row['id'] == tweet.id
    assert row['content'] == ''
    assert row['user_id'] == user1.id
    assert row['retweet_from'] == tweet_id


def test_retweet_fails_when_user_is_not_logged(user1: User):
    user1.save()
    with pytest.raises(TwitterError) as err:
        user1.retweet(1)
    assert str(err.value) == 'User midudev is not logged in!'


def test_retweet_fails_when_user_fails_login(user1: User):
    user1.save()
    user1.login('5678')
    with pytest.raises(TwitterError) as err:
        user1.retweet(1)
    assert str(err.value) == 'User midudev is not logged in!'


def test_retweet_fails_when_tweet_does_not_exist(user1: User):
    wrong_tweet_id = 99
    user1.save()
    user1.login(USER1_PASSWORD)
    with pytest.raises(TwitterError) as err:
        user1.retweet(wrong_tweet_id)
    assert str(err.value) == f'Tweet with id {wrong_tweet_id} does not exist!'


def test_get_tweets(user1: User):
    user1.save()
    user1.login(USER1_PASSWORD)
    tweet1 = user1.tweet('Red')
    tweet2 = user1.tweet('Green')
    tweet3 = user1.tweet('Blue')

    tested_tweets = (tweet1, tweet2, tweet3)
    all_tweets = user1.tweets
    isinstance(all_tweets, Generator)
    for tweet, tested_tweet in zip(all_tweets, tested_tweets):
        assert tweet.id == tested_tweet.id
        assert tweet.content == tested_tweet.content
        assert tweet.id == tested_tweet.id
        assert tweet.retweet_from == tested_tweet.retweet_from


def test_user_representation(user1: User, user2: User):
    assert str(user1) == 'midudev: Frontend developer'
    assert str(user2) == 'mouredev: Backend developer'


def test_build_user_from_db_row(user2: User, db_con: sqlite3.Connection):
    user2.save()

    db_cur = db_con.cursor()
    sql = 'SELECT * FROM user WHERE id=?'
    result = db_cur.execute(sql, (user2.id,))
    row = result.fetchone()

    tested_user = User.from_db_row(row)
    assert user2.id == tested_user.id
    assert user2.username == tested_user.username
    assert user2.password == tested_user.password
    assert user2.bio == tested_user.bio


def test_build_tweet(tweet1: Tweet):
    assert isinstance(tweet1.con, sqlite3.Connection)
    assert tweet1.con.row_factory == sqlite3.Row
    assert isinstance(tweet1.cur, sqlite3.Cursor)

    assert tweet1._content == 'This is just fine'
    assert tweet1.retweet_from == 0
    assert tweet1.id == 0

    tweet = Tweet(retweet_from=1)
    assert tweet._content == ''
    assert tweet.retweet_from == 1
    assert tweet.id == 0

    tweet = Tweet(content='Test', tweet_id=1)
    assert tweet._content == 'Test'
    assert tweet.retweet_from == 0
    assert tweet.id == 1


def test_tweet_is_retweet(tweet1: Tweet, tweet2: Tweet):
    assert tweet1.is_retweet is False
    assert tweet2.is_retweet is True


def test_tweet_content(user1: User, tweet1: Tweet, tweet2: Tweet, db_con: sqlite3.Connection):
    assert tweet1.content == 'This is just fine'

    user1.save()
    db_cur = db_con.cursor()
    sql = 'INSERT INTO tweet VALUES (?, ?, ?, ?)'
    params = (1, 'Be careful', user1.id, 0)
    db_cur.execute(sql, params)
    db_con.commit()
    assert tweet2.content == 'Be careful'


def test_save_tweet(tweet1: Tweet, user1: User, db_con: sqlite3.Connection):
    tweet1.save(user1)
    db_cur = db_con.cursor()
    sql = 'SELECT * FROM tweet WHERE id=?'
    result = db_cur.execute(sql, (tweet1.id,))
    row = result.fetchone()
    assert tweet1.id == row['id']
    assert tweet1.content == row['content']
    assert user1.id == row['user_id']
    assert tweet1.retweet_from == row['retweet_from']


def test_tweet_representation(tweet1: Tweet, tweet2: Tweet, user1: User, user2: User):
    tweet1.save(user1)
    assert str(tweet1) == '🐦 This is just fine (id=1)'
    tweet2.save(user2)
    assert str(tweet2) == '🔁 This is just fine (id=2)'


def test_build_tweet_from_db_row(user1: User, tweet1: Tweet, db_con: sqlite3.Connection):
    tweet1.save(user1)

    db_cur = db_con.cursor()
    sql = 'SELECT * FROM tweet WHERE id=?'
    result = db_cur.execute(sql, (tweet1.id,))
    row = result.fetchone()

    tested_tweet = Tweet.from_db_row(row)
    assert tweet1.id == tested_tweet.id
    assert tweet1.content == tested_tweet.content
    assert tweet1.retweet_from == tested_tweet.retweet_from


def test_build_twitter_object(twitter: Twitter):
    assert isinstance(twitter.con, sqlite3.Connection)
    assert twitter.con.row_factory == sqlite3.Row
    assert isinstance(twitter.cur, sqlite3.Cursor)


def test_add_user(twitter: Twitter, db_con: sqlite3.Connection):
    user = twitter.add_user('vanrossum', '=234aDF*', 'GOAT of Python')
    assert user.username == 'vanrossum'
    assert user.password == '=234aDF*'
    assert user.bio == 'GOAT of Python'
    assert user.id > 0

    db_cur = db_con.cursor()
    sql = 'SELECT * FROM user WHERE id=?'
    result = db_cur.execute(sql, (user.id,))
    row = result.fetchone()
    assert user.username == row['username']
    assert user.password == row['password']
    assert user.bio == row['bio']
    assert user.id == user.id


def test_add_user_for_valid_regex_password(twitter: Twitter):
    VALID_PASSWORDS = ('=78Fu!', '@932SwU*', '=1290RsOn!')
    for i, password in enumerate(VALID_PASSWORDS):
        username = f'user{i}'
        twitter.add_user(username, password, 'testing')


def test_add_user_for_invalid_regex_password(twitter: Twitter):
    INVALID_PASSWORDS = ('=7Fu!', '-932SwU*', '=1290RsOnT!')
    for i, password in enumerate(INVALID_PASSWORDS):
        username = f'user{i}'
        with pytest.raises(TwitterError) as err:
            twitter.add_user(username, password, 'testing')
        assert str(err.value) == 'Password does not follow security rules!'


def test_get_user(user1: User, twitter: Twitter):
    user1.save()
    tested_user = twitter.get_user(user_id=1)
    assert isinstance(tested_user, User)
    assert user1.username == tested_user.username
    assert user1.password == tested_user.password
    assert user1.bio == tested_user.bio


def test_get_user_fails_when_user_id_does_not_exist(user1: User, twitter: Twitter):
    with pytest.raises(TwitterError) as err:
        twitter.get_user(user_id=3)
    assert str(err.value) == 'User with id 3 does not exist!'
