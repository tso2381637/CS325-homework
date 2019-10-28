
def max_wis(a,max_num=None):	
	n = len(a)
	if max_num is None:
		max_num={}
	if n <=0:
		return 0,[]	
	elif n not in max_num:
		b, blst = max_wis(a[:-2],max_num)
		c, clst = max_wis(a[:-1],max_num)
		if a[n-1]>0:
			b += a[n-1]
		if b>c :
			blst.append(a[n-1])
			max_num[n] = (b, blst)
		else:
			max_num[n] = (c, clst)
		#print(max_num)

	return max_num[n]
		




print(max_wis([-1,8,10]))
print(max_wis([63229, 7871, 74587, 59445, 71381, 5404, 56721, 41863, 62960, 42424, 37376, 38654, 9686, 88564, 71093, 69118, 26876, 44293, 48730, 2476, 58586, 23466, 4192, 48799, 15818, 28847, 82565, 71941, 95094, 64294, 79614, 16219, 16348, 37528, 57940, 73917, 31890, 80693, 88456, 82255, 39260, 8070, 36726, 87408, 44400, 85485, 88349, 45095, 66399, 12786, 99639, 19331, 63101, 72119, 20801, 69561, 33307, 66400, 9388, 41212, 63564, 85236, 72617, 4787, 97918, 32153, 58247, 8466, 68896, 93322, 21028, 18211, 55043, 24187, 13768, 17505, 54214, 71736, 5284, 41499, 87421, 42354, 64137, 77183, 31897, 40971, 94056, 85477, 17893, 95807, 77428, 13186, 51169, 48753, 36957, 27003, 78557, 93281, 84281, 99236]))