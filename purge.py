import firebase_admin
from firebase_admin import auth
from google.cloud import firestore
import google.cloud.exceptions



input = input('type "confirm purge" to confirm user purge: ')

if input == 'confirm purge':
    print('PURGE CONFIRMED')
else:
    print('PURGE DENIED, QUITTING')
    quit()



default_app = firebase_admin.initialize_app()

# Start listing users from the beginning, 1000 at a time.
page = auth.list_users()
while page:
    for user in page.users:
        print('User: ' + user.uid)
        auth.delete_user(user.uid)
        print('Successfully deleted user')
    # Get next batch of users.
    page = page.get_next_page()

# Iterate through all users. This will still retrieve users in batches,
# buffering no more than 1000 users in memory at a time.
for user in auth.list_users().iterate_all():
    print('User: ' + user.uid)

db = firestore.Client()

# [START delete_full_collection]
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).get()
    deleted = 0

    for doc in docs:
        delete_subcollection(db.collection(u'users').document(doc.id).collection(u'whitelist'), 1000)
        print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
        doc.reference.delete()
        deleted = deleted + 1
# [END delete_full_collection]

# [START delete_full_collection]
def delete_subcollection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).get()
    deleted = 0

    for doc in docs:
        print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
        doc.reference.delete()
        deleted = deleted + 1
# [END delete_full_collection]

delete_collection(db.collection(u'users'), 1000)
