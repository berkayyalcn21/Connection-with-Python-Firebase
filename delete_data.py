import firebase_admin
from firebase_admin import credentials, firestore

#Setup
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

"""
# Delete data - known ID
db.collection("people").document("CFCK3UoJYjcVtEfo6AqV").delete()


# Delete data - known ID - field
db.collection("people").document("student").update({"agegroup": firestore.DELETE_FIELD})"""


# Delete docs - unkown ID - first way
"""
docs = db.collection('people').get()
for doc in docs:
    key = doc.id
    db.collection('people').delete()
"""

# Delete docs - unkown ID - second way (Şartlı silme)
"""docs = db.collection('people').where("age", ">=", 22).get()
for doc in docs:
    key = doc.id
    db.collection('people').document(key).delete()"""

# Delete docs - unkown ID - thirth way (Döküman içinden belirli kaydı silme)
"""docs = db.collection('people').where("age", ">=", 22).get()
for doc in docs:
    key = doc.id
    db.collection('people').document(key).update({"age": firestore.DELETE_FIELD, "name": firestore.DELETE_FIELD})"""










