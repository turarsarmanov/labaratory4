from datetime import datetime

a1 = input()
a2 = input()
date1 = datetime.strptime(a1, "%x")
date2 = datetime.strptime(a2, "%x")

diff = abs((date2 - date1).total_seconds())
print(int(diff))