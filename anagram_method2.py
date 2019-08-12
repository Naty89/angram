def anagram(x, y):

	return sorted(x.replace(" ","").lower()) == sorted("".join(y))

print(anagram("Chris Pratt", ["chirps", "ratt"]))
