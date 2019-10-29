def num_no(n,dict=None):


	if dict == None : dict={0:1,1:2,2:3}

	if n not in dict:

		dict[n] = num_no(n-1) + num_no(n-2)


	return dict[n]



def num_yes(n,dict=None):



	
	if dict == None : dict={0:1,1:2,2:3}

	if n not in dict:

		dict[n] = num_no(n-1) + num_no(n-2)


	return pow(2,n) - dict[n]




print(num_yes(5))
print(num_no(5))