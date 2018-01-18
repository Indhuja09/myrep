set_password = "changeme"
attempts = 0
while True: 
   password = input("Enter password: ")
   attempts+=1
   if password == set_password: 
       print("Password accepted")
       break
   else:
       print("Incorrect password")
       if attempts > 5:
           print("Exceeded attempts, Access Denied")
           break
print( "You had " +str(attempts) +" attempts to guess the password")
