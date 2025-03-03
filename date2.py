import datetime
yesterday = datetime.datetime.today()-datetime.timedelta(days=1)
print("yesterday :",yesterday)
today = datetime.datetime.today()
print("today :",today)
tomorrow = datetime.datetime.today()+datetime.timedelta(days=1)
print("tomorrow :",tomorrow)
