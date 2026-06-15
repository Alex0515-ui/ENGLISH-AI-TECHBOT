from entities.models import User, User_words, Word_Status
from sqlalchemy.orm import Session
from datetime import  datetime, timedelta, timezone

class WordService:

    
    @staticmethod
    def save_word_to_db(db: Session, tg_id: int, word_id: int):
        """Saves word to db"""

        user = db.query(User).filter(User.telegram_id==tg_id).first()

        existing = db.query(User_words).filter_by(user_id=user.id, word_id=word_id).first()
        if existing:
            return existing
        
        next_review = datetime.now(timezone.utc) + timedelta(days=1)

        word = User_words(
            word_id=word_id,
            user_id=user.id,
            status=Word_Status.LEARNING,
            repetition_stage=0,
            next_review_date=next_review
        )

        db.add(word)
        db.commit()
        db.refresh(word)

        return word


    @staticmethod
    def process_answer(db: Session, word: User_words, correct: bool):
        """Progress in learning words"""

        REVIEW_INTERVALS = {
            0: 1,               # Repeat after 1 day
            1: 3,               # Repeat after 3 days
            2: 5,               # Repeat after 5 days
            3: 7                # Repeat after 7 days
        }
        
        if correct:
            word.repetition_stage += 1
            if word.repetition_stage >= 4:
                word.status = Word_Status.LEARNED
                word.next_review_date = None
            else:
                days = REVIEW_INTERVALS[word.repetition_stage]
                word.next_review_date = datetime.now(timezone.utc) + timedelta(days=days)

        else:
            word.repetition_stage = 0
            word.next_review_date = datetime.now(timezone.utc) + timedelta(days=1)
        
        db.commit()

        return word


    @staticmethod
    def get_words_to_repeat(db: Session, tg_id: int, now=None):
        """Getting words to repeat them"""

        if not now:
            now = datetime.now(timezone.utc)
        user = db.query(User).filter(User.telegram_id == tg_id).first()
        data = db.query(User_words).filter(User_words.next_review_date <= now, User_words.user_id == user.id).all()
        return data


    

    

    
