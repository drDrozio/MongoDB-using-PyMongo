import pymongo
from pymongo import MongoClient
import urllib,csv

with open('creds.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
    	clid=row[0]
    	pwd=row[1]
csv_file.close()

cluster=MongoClient("mongodb+srv://"+clid+":"+pwd+"@cluster0.qjtkv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster['test']
collection=db['test']

##Inserting Data/Create
post={"_id":0,"name":"tim","score":5}
post1={"_id":10,"name":"iban","score":15}
post2={"_id":13,"name":"batuta","score":20}
#collection.insert_one(post)
# collection.insert_many([post1,post2])


##Find/Retrieve
results=collection.find({"name":"batuta","score":20})
for result in results:
	id=result['_id']
res=collection.find_one({"_id":id})
print(res)

#Find All
xs=collection.find({})
for x in xs:
	print(x)


# #Deletion
# collection.delete_one({"name":"tim"})
# #delete_many works same as insert_many


# #Updation
# #collection.update_one({"_id":10},{"$set":{"score":11}})
# #Adding fields using update
# collection.update_one({"_id":13},{"$set":{"comments":"Good boy"}})


#Other Queries:-
#Count of Documents
post_count=collection.count_documents({})
print("Number of Documents : ",post_count)
#Count of people with score more than 12
q1=collection.find({"score":{"$gt":12}}).count()
print("Scorers greater than 12 : ",q1)