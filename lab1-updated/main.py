def divideP(P):
	grpArr = []
	for items in P:
		if P == ')':
			grpArr.append(P.all)
			break
	return grpArr

def createGroup(grpArr):
	count = 0
	array1 = []
	array2 = []
	for items in grpArr:
		if items == ')' and (items + 1) is not None:
			count+= 1
	for i in count:
		if grpArr[i] == '(' and count == 0:
			array1.append(grpArr[i])
		elif grpArr[i] == '(' and count == 1:
			array2.append(grpArr[i])
		elif grpArr[i] == ')':
			array1.append(grpArr)
		else:
			next
	return array1, array2

def createArrayGroups(array1, array2):
	count = 0
	for items1, items2 in array1, array2:
		if items1 == '(' or items1 == ')' or items1 == '^' or items1 == 'v' or items1 == '~' or items1 == '@':
			count += 1
	
	return count

def isSatisfiable(P):
	for i in range(len(P)):
		if i != ')':
			if i == '^':
				orFunc = createGroup(divideP(P))
				if i + 1 is not None:
					boolean = orFunc or i + 1
			elif i == 'v':
				andFunc = createGroup(divideP(P))
				if i + 1 is not None:
					boolean = andFunc and i + 1
			elif i == '@':
				xOr = createGroup(divideP(P))
				if i + 1 is not None:
					boolean = xOr ^ i + 1
			elif i == '~':
				negation = not createGroup(divideP(P))
			else:
				next
		else:
			break
	return boolean

list_Q = ['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ]
print(isSatisfiable(list_Q))
			