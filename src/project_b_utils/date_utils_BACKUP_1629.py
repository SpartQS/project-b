from datetime import datetime


def get_current_date():
<<<<<<< HEAD
    return "DATE FROM DEVELOPER A"
=======
    return "DATE FROM DEVELOPER B"
>>>>>>> developer-b


def format_date(date):
    return date.strftime("%d.%m.%Y")