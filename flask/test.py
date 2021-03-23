import pyrebase

# firebase config
config = {
    "apiKey": "AIzaSyCgUIgDoR7tPBGjgxkMaGQxHcVhu2WSmUU",
    "authDomain": "capstone-af326.firebaseapp.com",
    "databaseURL": "https://capstone-af326-default-rtdb.firebaseio.com",
    "projectId": "capstone-af326",
    "storageBucket": "capstone-af326.appspot.com",
    "messagingSenderId": "851232030295",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# trying db
test = {"name": "Jane", "gender": "Female", "3": [1, 2, 3, 4, ]}
db.child("test").push(test)
