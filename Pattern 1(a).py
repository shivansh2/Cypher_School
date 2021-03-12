def pattern(n):
		  space=n
		  for i in range(1,n+1):
		  	for j in range(0,space):
		  		print(" ", end="")
		  	for k in range(0,i):
		  		print("*", end="")
		  	space-=1
		  	print(" ")
		  	
		  	
		  	
		  	
n=int(input("Enter Number of Rows:"))
pattern(n)