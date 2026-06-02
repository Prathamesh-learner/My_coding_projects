for i in range(10):
  print(f"5 x {i+1} = {5*(i+1)}")

password = "password123"
counter = 0
print("Number of attempts left before lockout: 3")
while counter < 3:
  attempt = input("Enter your password: ")
  if attempt == password:
    print("The password you entered is correct.")
  else:
    print(f"You entered the wrong password: attempts remaining before lockout: {3 - (counter + 1)}")
    counter = counter + 1