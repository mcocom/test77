import csv
import random

csv_result = csv.reader(open(r'C:\Users\54529\Desktop\danci.csv'))
a = input("请输入日期")
b = []
for x in csv_result:
  if(x[2]!=""):
    e1 = x[2].split("-")
    e2 = a.split("-")
    if(int(e2[0])>int(e1[0]) or (int(e2[0])==int(e1[0])and int(e2[1])>=int(e1[1]))):
        b.append(x)
print(b)
print(len(b))
count = int(input("请输入出题个数"))
i = 1

while i<=count:
 c = random.randint(0,len(b)-1)
 d = random.randint(0,1)
 print("第{0}题为:{1}".format(i,b[c][d]))
 b.pop(c)
 i+=1

