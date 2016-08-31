########################################
#
# Functions2
#	
#	Instructions and definitions here: 
#	
#	github.com/mvhs-apcsp/functions2
#
#	Write the testing code first!
#	Then implement each function.
#
#	Don't forget to commit after each
#	function.
#
########################################


# TODO - write elevenish

def elevenish(n):
	return n % 11 == 0 or n % 11 == 1






print elevenish(11) #True
print elevenish(12) #True
print elevenish(13) #False
print elevenish(22) #True
print elevenish(23) #True
print elevenish(5) #False


print "\n"
# TODO - write ice_cream_party

def ice_cream_party(ice_cream, candy):
	if candy < 5 or ice_cream < 5:
		return 0
	elif (candy / ice_cream) == 2 or (ice_cream / candy) == 2:
		return 2
	elif candy >= 5 and ice_cream >= 5:
		return 1





print ice_cream_party(10,5) #2
print ice_cream_party(5,10) #2
print ice_cream_party(5,5) #1
print ice_cream_party(6,6) #1
print ice_cream_party(6,3) #0
print ice_cream_party(2,6) #0
print ice_cream_party(2,3) #0



print "\n"
# TODO - write successful_squirrel_party

def successful_squirrel_party(is_weekend, nuts):
	if is_weekend:
		if nuts > 40:
			return True
		else:
			return False
	else:
		if nuts > 40 and nuts < 60:
			return True
		else:
			return False


print successful_squirrel_party(True,50) #True
print successful_squirrel_party(True,70) #True
print successful_squirrel_party(False,70) #False
print successful_squirrel_party(False,20) #False
print successful_squirrel_party(False,50) #True



print "\n"
# TODO - write ticket

def ticket(a, b, c):
	if (a+b) == 10 or (c+b) == 10 or (a+c) == 10:
		return 10
	elif ((a+b) - (b+c)) >= 10:
		return 5
	elif ((a+b) - (a+c)) >= 10:
		return 5
	else:
		return 0




print ticket(10, 0, 4) #10
print ticket(13, 0, 10) #10
print ticket(0, 4, 10) #10
print ticket(30, 0, 15) #5
print ticket(15, 15, 0) #5
print ticket(2, 2, 2) #0

# TODO - write in_order

# TODO - write less_by_ten

# TODO - write fizz_string

# TODO - write first_last_six

# TODO - write rotate_left

# TODO - write double23