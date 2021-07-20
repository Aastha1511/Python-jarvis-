import json

def getUser():
  try:
    userFile = open(r'user_info\user.json',"r")
    user = json.load(userFile)
    if(user['name'] and user['gender'] and user['dob']):
      return user
  except:
    return None

def createNewUser(newUser):
  try:
    userFile = open(r'user_info\user.json','w')
    json.dump(newUser,userFile)
  except:
    print("Something went wrong")


    