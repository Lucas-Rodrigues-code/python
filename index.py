import datetime

date_str = "2024-12-05T14:52:09.271489"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

if type(date_obj) == datetime.datetime:
    print("É uma date!")

num = 10
if num>5:
    print("É uma date!")
elif num == 10 and num < 5:
    print("Não é uma date!")
else:
    print("Não é uma date!")