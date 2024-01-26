import csv
with open('sample.csv','w') as file:
    data=[
        [1,'yashwanth'],
        [2,'raju'],
        [3,'sus'],
    ]
    record=csv.writer(file)
    record.writerows(data)