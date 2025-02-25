import datetime
a = input()

finalList = []
for i in range(a):
    b = input()
    splitedList = b.split(',')
    splitedList = [i for i in splitedList if i != '']
    splitedList[0] = datetime.datetime.strptime(splitedList[0], '%y-%m-%d')
    finalList.append(splitedList)

for i in finalList:
    print(i)
    