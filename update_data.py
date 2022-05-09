import firebase_admin
from firebase_admin import credentials, firestore

#Setup
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# Update data - known key
"""db.collection('people').document('student').update({
    "age":35
})

db.collection('people').document('student').update({
    "country":"US"
})

db.collection('people').document('student').update({
    "age": firestore.Increment(10)
})

# Delete from db
db.collection('people').document('student').update({
    "social": firestore.ArrayRemove(['linkedin'])
})

# Add to db
db.collection('people').document('student').update({
    "social": firestore.ArrayUnion(['linkedin'])
})
"""

# Update data - unknown key
# First way
"""docs = db.collection('people').get()
for doc in docs:
    if doc.to_dict()['age']>=22:
        key = doc.id
        db.collection('people').document(key).update({"agegroup": "middle aged"})
"""

# Second way
"""docs = db.collection('people').where("age", ">=", 22).get()
for doc in docs:
    key = doc.id
    db.collection('people').document(key).update({"agegroup": "older than 22"})
"""

