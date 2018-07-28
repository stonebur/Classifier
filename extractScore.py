def extract(labels, results, file_name):
	if labels[0] == "like":
		like = results[0]
	else:
		like = results[1]

	f = open('likeScores', 'a')
	f.write('{:0.5f} {}\n'.format(like, file_name))
		
