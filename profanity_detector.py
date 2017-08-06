import urllib

def read_text():
	quotes = open("/Users/Alvin/GitHub/Python/Udacity-FS/movie_quotes_curse.txt","r")
	contents = quotes.read()
	print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	# print(output)
	if "true" in output:
		print("Profanity alert!!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")
	connection.close()

read_text()