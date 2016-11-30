def tri_bulle(t):

	for i in range(len(t) - 1):
		for j in range(len(t) - 1 - i):
			if t[j] > t[j+1]:
				c = t[j]
				t[j] = t[j+1]
				t[j+1] = c
	return t

print tri_bulle([6, 5, 4, 3, 2, 1])
