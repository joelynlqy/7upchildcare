import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init Firebase
def getFirebase():
  cred = credentials.Certificate('./APIModules/seproject-5cc64-574b67cbadfb.json')
  firebase_admin.initialize_app(cred)
  return firestore.client()