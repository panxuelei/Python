from zipfile import ZipFile

def extractFile(zip_file, password):
		try:
			zip_file.extractall(extract_folder, pwd=bytes(password, "utf-8"))
			return password
		except Exception as e:
			return

def main():
	zip_file = ZipFile("password1234.zip")
	extract_folder = "temp" # extract zip file to this folder.
	dictionary = "dictionary.txt" # password file
	i = 0 # failed password

	extractFile(zip_file, "1234")

	# with open(dictionary, 'r') as d:
	# 	for line in d.readlines():
	# 		password = line.strip("\n") # each password 
	# 		guess = extractFile(zip_file, "1234")
	# 		print(guess)
	# 		i += 1

	# 		if guess:
	# 			print("[+] Password = " + password)
	# 			print(str(i) + " password failed.")
	# 			exit(0)


if __name__ == '__main__':
	main()





	
