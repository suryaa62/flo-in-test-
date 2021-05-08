#this file is for testing
import collect_training_data
import recognize
import classifier

while(True):
    k = int(input("1 -> register user\n2 -> authenticate existing user\n3-> exit: "))
    print(k)
    if(k==3):
        break
    elif(k==1):
        username = input("Enter user name: ")
        userid = input("Enter user id: ")
        collect_training_data.register_user(username,userid)
        classifier.train_classifier('data',username,userid)
    elif(k==2):
        username = input("Enter user name: ")
        userid = input("Enter user id: ")
        recognize.authenticate_user(username,userid)
    else:
        print("Enter Valid Key")