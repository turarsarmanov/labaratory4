import datetime
date = datetime.datetime.now()
datenms = date.replace(microsecond=0)
print(datenms)