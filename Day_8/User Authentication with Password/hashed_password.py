# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# password = "my name is Yash pathak"

# hashed_password = bcrypt.generate_password_hash(password =password)
  
# check =bcrypt.check_password_hash(hashed_password,"my name is Yash pathak" )
# print(check)



from werkzeug.security import generate_password_hash,check_password_hash

#here i am creating the hashed passsword
hashed_pass =  generate_password_hash('mypassword')
print(hashed_pass)

#here i am checking the hashed password
check = check_password_hash(hashed_pass,'mypassword')
print(check)
