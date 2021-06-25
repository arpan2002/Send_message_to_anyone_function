import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("number of friends:"))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends =  client.getUsers(name)
    # return a list of name
    friend = friends[0]
    msg = str(input("message: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("message sent sucessfully!")
    else:
        print("ERROR404 in sending message ")    
    
    