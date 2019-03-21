import requests
import pprint
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init Firebase
cred = credentials.Certificate('seproject-5cc64-574b67cbadfb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def urlToListOfJsonObjects(url):
  """
  Helper method to call API and convert it to a list containing JSON objects
  """
  res = requests.get(url)
  resultJson = res.json()
  return resultJson['result']['records']

# Childcare details api
centreDetailsAPI = 'https://data.gov.sg/api/action/datastore_search?resource_id=4fc3fd79-64f2-4027-8d5b-ce0d7c279646&limit=1030'
# Price api
centrePriceAPI = 'https://data.gov.sg/api/action/datastore_search?resource_id=0c14ceec-da1b-43c6-92fc-e82d7219840b&limit=20584'

# Childcare details json
list_of_json_object = urlToListOfJsonObjects(centreDetailsAPI)
list_of_json_object2 = urlToListOfJsonObjects(centrePriceAPI)

# for i in list_of_json_object:
#   centreID = i['centre_code']
#   doc_ref = db.collection(u'centres').document(str(centreID))
#   doc_ref.set(i)

for i in list_of_json_object:
  # First layer of collections
  centreID = i['centre_code']
  doc_ref = db.collection(u'centres').document(str(centreID))
  doc_ref.set(i)
  for j in list_of_json_object2:
    # Second layer of collections
    detailID = j['centre_code']
    if (detailID == centreID):
     doc_ref_two = db.collection(u'centres').document(str(centreID)).collection(u'details').document(str(j['_id']))
     doc_ref_two.set(j)



