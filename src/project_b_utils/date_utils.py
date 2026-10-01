from datetime import datetime



def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def format_date(date):
    return date.strftime("%d.%m.%Y")

