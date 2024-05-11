import re
email_condition="^[a-z]+[\.__]?+[0-9 a-z]+[@]\w+[\.]\w{2,3}$"
email=input("Please enter your email : ")
if(re.search(email_condition,email)):
    print("Right email")
else:
    print("try agian")