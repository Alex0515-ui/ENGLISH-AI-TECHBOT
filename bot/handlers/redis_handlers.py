import json
from db.config import redis_client
from datetime import date


# ============ LEARNING WORDS ===============


async def get_session(tg_id: int):
    """Get learning session from Redis"""

    data = await redis_client.get(f"session:{tg_id}")
    return json.loads(data) if data else None


async def update_session(tg_id: int, session: dict):
    """Updates learning session from Redis"""

    await redis_client.set(f"session:{tg_id}", json.dumps(session), ex=3600)


# ============ DAILY LIMITS ===============================


async def get_daily(tg_id: int):
    """Checks daily limit of learning words session from Redis"""

    data = await redis_client.get(f"daily:{tg_id}")
    return json.loads(data) if data else None

async def set_daily(tg_id: int, date: str):
    """Sets daily limit of learning words to Redis"""

    await redis_client.set(f"daily:{tg_id}", json.dumps({"last_date": date}), ex=172800)

async def finish_learning(tg_id:int):
    """Completes learning limit"""

    today = str(date.today())
    data = {
        "last_date": today
    }
    await redis_client.set(f"daily:{tg_id}", value=json.dumps(data), ex=172000)


async def get_daily_dialogue(tg_id:int):
    """Gets daily AI limit from Redis"""

    data = await redis_client.get(f"daily_dialogue:{tg_id}")
    if data:
        return json.loads(data)
    
async def set_daily_dialogue(tg_id:int, date: str):
    """Sets daily AI limit to Redis"""

    await redis_client.set(f"daily_dialogue:{tg_id}", json.dumps({"last_date": date}), ex=172800)


# ======== REPEATING WORDS ==============================


async def get_repeat_session(tg_id: int):
    """Gets session of repeating word from Redis"""
    data = await redis_client.get(f"repeat:{tg_id}")
    return json.loads(data) if data else None

async def set_repeat_session(tg_id: int, session: dict):
    """Updates session of repeating words to Redis"""
    await redis_client.set(f"repeat:{tg_id}", json.dumps(session), ex=18000)


# ================ DIALOGUE WITH AI ===================


async def get_chat_dialogue(tg_id:int):
    """Gets chat's memories"""

    data = await redis_client.get(f"dialogue:{tg_id}")
    if data:
        return json.loads(data)

async def save_chat_dialogue(tg_id:int, history: dict):
    """Set memories to chat"""

    await redis_client.set(f"dialogue:{tg_id}", json.dumps(history))


# ============ WORD PRACTISE  =========

async def get_practise(tg_id: int):
    """Gets temporary storage for words"""

    data = await redis_client.get(f"practise:{tg_id}")
    if data:
        return json.loads(data)
    
async def set_practise(tg_id: int, data):
    """Sets to temporary storage words that user practising"""

    await redis_client.set(f"practise:{tg_id}", json.dumps(data))

async def get_session_practise(tg_id: int):
    """ Gets words for practise from Redis"""
    data = await redis_client.get(f"practise_session:{tg_id}")
    if data:
        return json.loads(data)

async def set_session_practise(tg_id: int, data):
    """Set words for practies to Redis"""
    await redis_client.set(f"practise_session:{tg_id}", json.dumps(data), ex=21600)












