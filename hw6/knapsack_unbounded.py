

def best(w, items, opt=None,):
	print(w,items)
	if opt is None:
		opt = {}

	for i in range(len(items)-1,0):
		if w in opt and i in opt[w]:
			return opt[w][i]
		w_i, v_i, c_i = items[i]

		if w >= w_i:
			number = min(w//w_i,c_i)

			t, t_i = best(w-(number*w_i),items[:-1],opt)
			nt, nt_i = best(w,items[:-1],opt)
			if t+(number*v_i) >= nt:
				t_i[i] += number
				opt[w][i] = t+(number*v_i),t_i[i]
			else:
				opt[w][i] = nt, nt_i
		elif w==0:

			opt[w][i] = 0,[0]*len(items)

	return opt[w][i]


best(3, [(1, 5, 2), (1, 5, 3)])
#best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
#best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])


		


