import datetime
def date_time():
    now = datetime.datetime.now()
    print("Pynox Time Service")
    print("--------------------")
    print(datetime.date.today())
    print(f"{now.hour}:{now.minute}:{now.second}")