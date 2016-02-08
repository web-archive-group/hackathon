from pymongo import MongoClient

# connection to MongoDB on the IFO server
uri = "mongodb://hackathon_reader:To0305@www.oci-ifo.org:27017/scrapy?authMechanism=MONGODB-CR"
client = MongoClient(uri)
db = client.scrapy    
collection = db.websites

#uncomment to save output to file
#f = open('data.txt', 'w') 

#Query to MongoDB
#This query outputs a list media in the database.
media = collection.find({"original_website_url": {"$exists" : 1}}).limit( 1000 )
for x in media:
    print x
#uncomment to save output to file
#    print  >>f, x 

