import firebase_admin
from firebase_admin import auth
from google.cloud import firestore
import google.cloud.exceptions
import random
import csv

default_app = firebase_admin.initialize_app()

NUMBER_OF_USERS = 600

db = firestore.Client()

firstNamesFile = open('firstNames.txt', 'r')
firstNames = firstNamesFile.read().split('\n')
firstNamesFile.close()

lastNamesFile = open('lastNames.txt', 'r')
lastNames = lastNamesFile.read().split('\n')
lastNamesFile.close()

zipCodesFile = open('zipCodes.txt', 'r')
zipCodes = zipCodesFile.read().split('\n')
zipCodesFile.close()

zipCodesToValues = list(csv.reader(open("zipCodesToValue.csv")))

accountTypes = ['Student', 'Tutor']
genders = ['Male', 'Female', 'Other']
interests = ['STEM', 'The Arts', 'Other']
races = ['Asian American', 'African American', 'Native American', 'Pacific Islander', 'White American']

for i in range(NUMBER_OF_USERS):
    firstName = random.choice(firstNames)
    lastName = random.choice(lastNames)
    email = firstName + lastName + '@example.com'
    password = email.lower()
    accountType = random.choice(accountTypes)
    zipCode = random.choice(zipCodes)

    value = ""

    for entry in zipCodesToValues:
        if entry[0] == zipCode:
            value = float(entry[1].strip())

    gender = random.choice(genders)
    interest = random.choice(interests)
    race = random.choice(races)

    try:
        user = auth.create_user(
        email=email,
        password=password,
        display_name=firstName + ' ' + lastName,)
    except:
        print('an exception occured')
        continue

    data = {
        u'accountType': accountType,
        u'zipCode': zipCode,
        u'value': value,
        u'gender': gender,
        u'interest': interest,
        u'race': race,
        u'firstName': firstName,
        u'photoURL': "https://media.istockphoto.com/vectors/flat-style-square-shaped-female-character-icon-with-shadow-vector-id473482490?k=6&m=473482490&s=612x612&w=0&h=f9F_64YCHu1_UiOJVb6PPQyMYatfVPBW9j7M19Yjn18="
    }

    db.collection(u'users').document(user.uid).set(data)

    print('Sucessfully created new user: {0}'.format(user.uid))
