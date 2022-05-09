import firebase_admin
from firebase_admin import credentials, firestore

#Setup
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add document with auto IDs
"""data = {
    'name': 'berkay'.title(),
    'surname': 'yalçın'.title(),
    'age': 23,
    'employed': True
}"""
#db.collection('people').add(data)

# Set document with known IDs
"""data = {
    'name': 'recep'.title(),
    'surname': 'yalçın'.title(),
    'age': 23,
    'employed': True
}"""

"""db.collection('people').document('student').set(data)"""

# Merging
"""db.collection('people').document('student').set({'country': 'Turkey'}, merge=True)"""

# Set document with auto IDs
"""db.collection('people').document().set(data)"""


# Collection in document
"""db.collection('person').document('school').collection('lessons').add({'name': 'test'})"""
"""db.collection('person').document('school').collection('lessons').document('adVer').set({'name': 'test', 'surname': 'test2'})"""























