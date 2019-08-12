def anagram(x, y):
	l = []
	o = "".join(y)
	p = x.replace(" ", "")
	e = p.lower()
	if len(e) == len(o):
		for i in o:
			if i in e:
				l.append(True)
			else:
				l.append(False)
	else:	
		return False

	return all(l)

print(anagram("Chris Pratt", ["chirps", "rat"]))