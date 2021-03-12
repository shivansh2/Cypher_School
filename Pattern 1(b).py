n= int(input("Enter the Number Of Rows:"))
k=65
for i in range(0,n):
	for j in range(0,i+1):
			ch=chr(k)
			print(ch, end=" ")
			k=k+1
	print(" ")