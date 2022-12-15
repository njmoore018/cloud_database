import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('cloud-database-practice-firebase-adminsdk-14v89-510255ff8c.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

obj1 = {
    'Name': 'Mike',
    'Age': 100,
    'Net Worth': 1000000000
}

obj2 = {
    'Name': 'Tony',
    'Age': 10,
    'Net Worth': 10000000
}

data = [obj1, obj2]

for record in data:
    doc_ref = db.collection(u'users').document(record['Name'])
    doc_ref.set(record)