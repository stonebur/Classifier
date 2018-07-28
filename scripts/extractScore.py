def extract(labels, results):
	if labels[0] == "like":
		like = results[0]
	else:
		like = results[1]
	print(like)