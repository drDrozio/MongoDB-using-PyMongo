import pymogo
from pymongo import MongoClient

cluster=MongoClient('mongodb+srv://Drozio:RandiRaina69@cluster0.qjtkv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=cluster['test']
collection=db['test']

 

