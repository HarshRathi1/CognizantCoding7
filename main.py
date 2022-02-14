n=21212
temp=n
r=0
if n>0:
   while temp>0:
      a = temp % 10
      r = r * 10 + a
      temp = temp // 10
else:
   print("Invalid input")
if n==r:
   print("Palindrome")
else:
   print("Not Palindrome")
#Code is Contributed by Harsh Rathi