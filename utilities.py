from datetime import datetime

def dateString():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M")
    return str(dt_string)