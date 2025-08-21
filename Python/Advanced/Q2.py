#Implement a simple shopping cart system using lists to add, remove, and display items.
cart=[]
while True:
	print("1.To add items in the cart")
	print("2.To remove an item from cart")
	print("3.To display cart items")
	print("4.To exit")
	ch=int(input("Enter your choice:"))
	if ch==1:
		item=input("Enter the item:")
		cart.append(item)
	elif ch==2:
		rm=input("Enter the item to remove:")
		if rm in cart:
			print(f"{rm} has been removed")
			cart.remove(rm)
		else:
			print(f"{rm} item not found in cart")
	elif ch==3:
		for items in cart:
			print(items)
	elif ch==4:
		break
	else:
		print("Please Enter a valid Choice")
