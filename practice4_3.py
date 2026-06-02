a = input("Enter the number you want the multiplication table of: ")

for i in range(10):
  product = (i + 1)*int(a)
  print(f"{a} x {i+1} = {product}")

for i in range(30):
  if (i+1) % 2 == 0:
    print(f"{i+1} is even")
  else: 
    print(f"{i+1} is odd")