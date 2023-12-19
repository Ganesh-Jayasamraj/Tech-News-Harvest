import os, firebase_admin
from dotenv import load_dotenv, find_dotenv
from firebase_admin import credentials, firestore

load_dotenv(find_dotenv())

databaseURL = os.environ.get('databaseURL')
Certificate_Path = os.environ.get("Certificate_Path")

cred = credentials.Certificate(Certificate_Path)
firebase_admin.initialize_app(cred)
# firebase_admin.initialize_app(cred, {
#     'databaseURL' : databaseURL
# })

db = firestore.client()

def add_new_usermail(usermail):
    try:
        doc_ref = db.collection(u'subscribers').document()
        doc_ref.set({
            u'mail-id':usermail
        })
        print("Successfully added to database")

    except Exception:
        print(Exception)

def remove_duplicate_values(to_remove):
    remove_list = list(dict.fromkeys(to_remove))
    return remove_list

def fetch_usermails():
    doc_ref = db.collection(u'subscribers')
    docs = doc_ref.get()

    receivers_mail = []

    for doc in docs:
        my_dict = doc.to_dict().copy()
        receivers_mail.append(my_dict['mail-id'])

    receivers_mail = remove_duplicate_values(receivers_mail)
    
    return receivers_mail

if __name__ == "__main__":
    add_new_usermail()
    fetch_usermails()
    remove_duplicate_values()