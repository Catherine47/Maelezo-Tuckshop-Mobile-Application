import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('Desktop\\TuckshopApp\\snack-n-stationery-hub.json')

firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('Students').document('Notebook')
doc_ref.set({
    'name': 'Notebook',
    'price': 100,
    'stock': 20,
    'offer': '10% off'
})
def read_data():
    doc_ref = db.collection('Students').document('Notebook')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Pen')
doc_ref.set({
    'name': 'Pen',
    'price': 20,
    'stock': 50,
    'offer': 'Buy 2 Get 1 free'
})
def read_data():
    doc_ref = db.collection('Students').document('Pen')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Pencil')
doc_ref.set({
    'name': 'Pencil',
    'price': 20,
    'stock': 100,
    'offer': 'No offers'
})
def read_data():
    doc_ref = db.collection('Students').document('Pencil')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Eraser')
doc_ref.set({
    'name': 'Eraser',
    'price': 25,
    'stock': 50,
    'offer': 'No offers'
})
def read_data():
    doc_ref = db.collection('Students').document('Eraser')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Sharpener')
doc_ref.set({
    'name': 'Sharpener',
    'price': 30,
    'stock': 120,
    'offer': 'No offers'
})
def read_data():
    doc_ref = db.collection('Students').document('Sharpener')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Ruler')
doc_ref.set({
    'name': 'Ruler',
    'price': 50,
    'stock': 80,
    'offer': '20% off'
})
def read_data():
    doc_ref = db.collection('Students').document('Ruler')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Glue Stick')
doc_ref.set({
    'name': 'Glue Stick',
    'price': 130,
    'stock': 40,
    'offer': 'Buy 1 Get 1 free'
})
def read_data():
    doc_ref = db.collection('Students').document('Glue Stick')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Stickynote')
doc_ref.set({
    'name': 'Stickynote',
    'price': 100,
    'stock': 50,
    'offer': '15% off'
})
def read_data():
    doc_ref = db.collection('Students').document('Stickynote')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Cupcakes')
doc_ref.set({
    'name': 'Cupcakes',
    'price': 25,
    'stock': 30,
    'offer': 'Buy 3 Get 1 free'
})
def read_data():
    doc_ref = db.collection('Students').document('Cupcakes')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Chips')
doc_ref.set({
    'name': 'Chips',
    'price': 100,
    'stock': 20,
    'offer': 'Buy 2 Get 1 free'
})
def read_data():
    doc_ref = db.collection('Students').document('Chips')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Soda')
doc_ref.set({
    'name': 'Soda',
    'price': 50,
    'stock': 20,
    'offer': 'No offers'
})
def read_data():
    doc_ref = db.collection('Students').document('Soda')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Chocolate')
doc_ref.set({
    'name': 'Chocolate',
    'price': 70,
    'stock': 15,
    'offer': '10% off'
})
def read_data():
    doc_ref = db.collection('Students').document('Chocolate')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Candy')
doc_ref.set({
    'name': 'Candy',
    'price': 10,
    'stock': 100,
    'offer': 'Buy 5 Get 1 free'
})
def read_data():
    doc_ref = db.collection('Students').document('Candy')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Ice Cream')
doc_ref.set({
    'name': 'Ice Cream',
    'price': 50,
    'stock': 40,
    'offer': 'Buy 1 Get 1 free'
})
def read_data():
    doc_ref = db.collection('Students').document('Ice Cream')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()
doc_ref = db.collection('Students').document('Cookies')
doc_ref.set({
    'name': 'Cookies',
    'price': 100,
    'stock': 30,
    'offer': '15% off'
})
def read_data():
    doc_ref = db.collection('Students').document('Cookies')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document.")

read_data()