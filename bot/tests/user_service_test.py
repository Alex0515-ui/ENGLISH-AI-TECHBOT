from services.user_service import UserService
from entities.models import *
from entities.schemas import UserCreateSchema

# ===== CREATE_USER TESTS ====================


def test_create_user_new(db):
    """Create user success"""

    data = UserCreateSchema(
        username="test1",
        telegram_id=123,
        first_name="Test"
    )

    user = UserService.create_user(db=db, data=data)

    assert user is not None
    assert user.telegram_id == 123
    assert user.first_name == "Test"



def test_create_user_existing(db):
    """User duplicate check to prevent double creation"""

    existing = User(telegram_id=123, first_name="Test")
    db.add(existing)
    db.commit()

    data = type("obj", (), {
        "telegram_id": 123,
        "username": "test",
        "first_name": "Test"
    })

    user = UserService.create_user(db=db, data=data)

    assert user.id == existing.id


# ========= GET_DAILY_WORDS TESTS =====

def test_get_daily_words_returns_words(db):
    """Fetch words for learning"""

    user = User(
        telegram_id=123,
        first_name="Test",
        level=Levels.A1,
        mode=Mode.GENERAL
    )
    db.add(user)
    db.commit()

    word = Words(
        word="run",
        translation="бегать",
        example="I run",
        level=Levels.A1,
        type=Mode.GENERAL
    )
    db.add(word)
    db.commit()

    result = UserService.get_daily_words(db=db, tg_id=123, word_count=5)

    assert result is not None
    assert len(result) == 1
    assert result[0]["word"] == "run"


def test_get_daily_words_excludes_learned(db):
    """Ensure learned words are not returned"""

    user = User(
        telegram_id=123,
        first_name="Alih",
        level=Levels.A1,
        mode=Mode.GENERAL
    )
    db.add(user)
    db.commit()

    word = Words(
        id=1,
        word="run",
        translation="бегать",
        example="I run",
        level=Levels.A1,
        type=Mode.GENERAL
    )
    db.add(word)
    db.commit()

    user_word = User_words(
        user_id=user.id,
        word_id=1
    )
    db.add(user_word)
    db.commit()

    result = UserService.get_daily_words(db=db, tg_id=123, word_count=5)

    assert result == []


def test_get_daily_words_no_user(db):
    """Do nothing if user does not exist"""
    result = UserService.get_daily_words(db=db, tg_id=999, word_count=5)

    assert result is None