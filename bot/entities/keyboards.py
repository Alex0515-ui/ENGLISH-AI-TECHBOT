from entities.models import Levels, Mode

# Main menu button
Main_menu_keyboard = {
    "keyboard": [ 
        [
            {"text": "Главное меню"}
        ]
    ],
    "resize_keyboard": True,
    "one_time_keyboard": False
}

# Main buttons
Menu_keyboard = {
    "inline_keyboard": [
        [
            {"text":"💬 Диалог с ИИ ассистентом", "callback_data": "start_dialogue"}
        ],
        [
            {"text": "📚 Учить слова", "callback_data": "set_learning"},
        ],
        [
            {"text": "⚙️ Выбрать режим", "callback_data": "choose_mode"},
        ],
        [
            {"text": "🎯 Выбрать уровень", "callback_data": "choose_level"},
        ]
    ]
}

# Choosing mode
Mode_keyboard = { 
    "inline_keyboard": [
        [
            {"text": f"{mode.name}", "callback_data": f"set_mode_{mode.name}"}
            for mode in Mode
        ]
        
    ]
    
}

# Choosing level
Level_keyboard = { 
    "inline_keyboard": [
        [
            {"text": f"{level.name}, ({level.value})", "callback_data": f"set_lvl_{level.name}"}
            for level in list(Levels)[i:i+2]
        ]
        for i in range(0, len(Levels), 2)
    ]
}

word_counts = [5, 10, 15, 20]

# Choosing words count to learn
Word_count_keyboard = {
    "inline_keyboard" : [
        [
            {"text": f"{count} слов",
             "callback_data": f"set_word_count_{count}"}
            for count in word_counts
        ]
    ]
}

# Repeat words button
Repeat_word_keyboard = {
    "inline_keyboard": [
        [
            {"text": "Давай!", "callback_data": "set_repeat"}
        ]
    ]
}

# Button that asks user, to review words
Practise_keyboard = {
    "inline_keyboard": [
        [
            {"text": "Давай", "callback_data": "set_practise_yes"},
            {"text": "Нет, не сегодня", "callback_data": "set_practise_no"}
        ]
    ]
}