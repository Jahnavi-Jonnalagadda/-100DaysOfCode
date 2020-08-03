# Python program to simplify a Unix 
# styled absolute path of a file 

# function to simplify a Unix - styled 
# absolute path 


def simplify(A): 
	# stack to store the file's names. 
	st = [] 

	# temporary string which stores the extracted 
	# directory name or commands("." / "..") 
	# Eg. "/a/b/../." 
	# dir will contain "a", "b", "..", "."; 
	dir = "" 

	# contains resultant simplifies string. 
	res = "" 

	# every string starts from root directory. 
	res += "/"

	# stores length of input string. 
	len_A = len(A) 
	i = 0
	while i < len_A: 

		# we will clear the temporary string 
		# every time to accomodate new directory 
		# name or command. 
		dir_str = "" 

		# skip all the multiple '/' Eg. "##/"" 
		while (i < len_A and A[i] == '/'): 
			i += 1
			print(dir_str)

		# stores directory's name("a", "b" etc.) 
		# or commands("."/"..") into dir 
		while (i < len_A and A[i] != '/'): 
			dir_str += A[i] 
			i += 1
			print(dir_str)

		# if dir has ".." just pop the topmost 
		# element if the stack is not empty 
		# otherwise ignore. 
		if dir_str == "..": 
			if len(st): 
				st.pop()
				print(dir_str)
			    

		# if dir has "." then simply continue 
		# with the process. 
		elif dir_str == '.': 
			continue

		# pushes if it encounters directory's 
		# name("a", "b"). 
		elif len(dir_str) > 0: 
			st.append(dir_str)
			print(dir_str)

		i += 1

	# a temporary stack (st1) which will contain 
	# the reverse of original stack(st). 
	st1 = [] 
	while len(st): 
		st1.append(st[-1]) 
		st.pop() 

	# the st1 will contain the actual res. 
	while len(st1): 
		temp = st1[-1] 

		# if it's the last element no need 
		# to append "/" 
		if (len(st1) != 1): 
			res += (temp + "/") 
		else: 
			res += temp 
		st1.pop() 

	return res 


# Driver code. 

# absolute path which we have to simplify. 
string = "/a/../"
res = simplify(string) 
print(res) 

# This code is contributed by ankush_953 

# https://leetcode.com/problems/simplify-path/
