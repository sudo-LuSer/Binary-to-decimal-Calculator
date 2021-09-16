#starting with name of allah "Bismilah !"
def BinaryToDecimal(arg):
	arg=int(arg)
	pwr=0;
	CountDecimal=0;
	strArg=str(arg)
	for _ in strArg:
		CountDecimal+=int(_)*(2**pwr)
		pwr+=1;
	return CountDecimal;
def run():
	print "\n"
	try:	
		In=int(input())
		Out=BinaryToDecimal(In)
		print(Out)
	except ValueError:
		print "Check your value please and enter a binary with 0 1 only !"
	run()
run()