import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import random

# Populate database with users and information from json file
def insert(db, people):
    for person in people:
        doc_ref = db.collection(u'users').document(people[person]['Name'])
        doc_ref.set(people[person])
    return

# Modify all users with randomized married status (true/false)
def modify(db, people):
    for person in people:
        num = random.randint(1,2)
        doc_ref = db.collection(u'users').document(people[person]['Name'])
        if num == 1:
            doc_ref.set({
                u'Married': True
            }, merge=True)
        else:
            doc_ref.set({
                u'Married': False
            }, merge=True)
    return

# Retrieve single user from database and display their information
def retrieve_person(db):
    person = input('\nEnter a name to retrieve information: ')
    doc_ref = db.collection(u'users').document(person)
    doc = doc_ref.get()
    info = doc.to_dict()
    name = info['Name']
    age = info['Age']
    sex = info['Sex']
    occupation = info['Occupation']
    married = info['Married']
    print(f'\nInformation about {name}')
    print(f'Age: {age}')
    print(f'Sex: {sex}')
    print(f'Occupation: {occupation}')
    print(f'Married: {married}')
    print()

# Display all user's names
def retrieve_all(db):
    docs = db.collection(u'users').stream()
    print()
    print('Users:')
    for doc in docs:
        print(doc.id)
    print()
    return

# Delete a user
def delete(db):
    retrieve_all(db)
    person = input('Enter a name to delete: ')
    db.collection(u'users').document(person).delete()
    return

# Display options list
def display_list():
    print('Please select a number from below:')
    print('1) Populate Database with users')
    print('2) Display all users')
    print('3) Add Random Marital Statuses')
    print('4) Retrieve user\'s data')
    print('5) Delete user')
    print('6) Quit')

# Run the program
def main():
    with open('people.json', 'r') as file:
        people = json.loads(file.read())
    cred = credentials.Certificate('cloud-database-practice-firebase-adminsdk-14v89-510255ff8c.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    option = 0
    while option != 6:
        display_list()
        option = int(input('> '))
        if option == 1:
            insert(db, people)
        elif option == 2:
            retrieve_all(db)
        elif option == 3:
            modify(db, people)
        elif option == 4:
            retrieve_person(db)
        elif option == 5:
            delete(db)
        elif option == 6:
            print('Thank you for using the program. Have a nice day!')
        else:
            print('That is not a valid option. Please try again.')
    return

if __name__ == '__main__':
    main()