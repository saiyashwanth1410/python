import csv
# with open('new.csv','w',newline='') as csvfile:
#     filednames=['id','name','age']
#     record=csv.DictWriter(csvfile,filednames)
#     record.writeheader()
#     data=[
#         {'id':1,'name':'saiyashwanth','age':22},
#         {'id':2,'name':'sureshraju','age':21},
#         {'id':3,'name':'niranjan sul','age':20},
#     ]
#     record.writerows(data)
with open('new.csv','r',newline='') as file:
    records=csv.DictReader(file)
    for i in records:
        print(i)