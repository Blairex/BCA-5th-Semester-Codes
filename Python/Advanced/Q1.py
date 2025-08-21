a=[[1,2],[3,4]]
b=[[1,2],[3,4]]
add=[]
multiply=[]
row=len(a)
col=len(a[0])

for i in range(row):
	s=[]
	m=[]
	for j in range(col):
		sum= a[i][j] + b[i][j]
		mul= a[i][j] * b[i][j]
		s.append(sum)
		m.append(mul)
	add.append(s)
	multiply.append(m)
print("Addition:",add)
print("Addition:",multiply)
