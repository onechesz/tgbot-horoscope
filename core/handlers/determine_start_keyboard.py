from core.data.__init__ import db
from core.keyboards.buttons.start_choice_keyboard import start_choice, start_choice_registered


def determine_keyboad(user_id):
    if not db.select_user_zodiac_sign(user_id=user_id)[0]:
        return start_choice

    return start_choice_registered
