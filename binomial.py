import math

exp = ""
def c(n, r):
	ui = int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))
	if ui != 1 and ui != 0:
		return ui
	else:
		return ""
	
def sub(n1):
	sub = ""
	n = str(n1)
	for t in range(0, len(n)):
		if n[t] == "1":
			sub += "¹"
		elif n[t] == "2":
			sub += "²"
		elif n[t] == "3":
			sub += "³"
		elif n[t] == "4":
			sub += "⁴"
		elif n[t] == "5":
			sub += "⁵"
		elif n[t] == "6":
			sub += "⁶"
		elif n[t] == "7":
			sub += "⁷"
		elif n[t] == "8":
			sub += "⁸"
		elif n[t] == "9":
			sub += "⁹"
		elif n[t] == "0":
			sub += "⁰"
	return sub

s = input()
x = s[1]
y = s[5]
op = s[3]
k = int(s[8:len(s)])
if op == "+":
	for i in range(k + 1):
		o = c(k, i)
		if k - i != 0 and k - i != 1:
			a = x + sub(k - i)
		elif k - i == 1:
			a = x
		else:
			a = ""
		
		if i != 0 and i != 1:
			b = y + sub(i)
		elif i == 1:
			b = y
		else:
			b = ""
		
		if exp == "":
			exp += str(o) + a + b
		else:
			exp += " + " + str(o) + a + b
			
elif op == "-":
	op1 = "+"
	for i in range(k + 1):
		o = c(k, i)
		if k - i != 0 and k - i != 1:
			a = x + sub(k - i)
		elif k - i == 1:
			a = x
		else:
			a = ""
		
		if i != 0 and i != 1:
			b = y + sub(i)
		elif i == 1:
			b = y
		else:
			b = ""
		
		if exp == "":
			exp += str(o) + a + b
		else:
			exp += " " + op1 + " " + str(o) + a + b
		
		if op1 == "-":
			op1 = "+"
		else:
			op1 = "-"
print()
print(exp)