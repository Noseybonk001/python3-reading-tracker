book_list = open("booklist.txt", "a")
choice = input("add new or see read ").lower()
if choice == "add new":
	wanna_quit = False
	while wanna_quit == False:
		book_name = input("book name: ")
		author_name = input("author name: ")
		fiction_or_non_fiction = input("f or nf ").lower()
		if fiction_or_non_fiction == "f":
			fiction_or_non_fiction = "fiction"
		elif fiction_or_non_fiction == "nf":
			fiction_or_non_fiction = "Non Fiction"
		book_rating = input("rate the book: ")
		book_list.write(f"{book_name}, {author_name}, {fiction_or_non_fiction}, {book_rating}" + "/10" + "\n")
		print(f"{book_name} has been added to your booklist")
		quit_option = input("Would you like to quit? y or n: ").lower()
		if quit_option == "y":
			wanna_quit = True
		elif quit_option == "n":
			pass
elif choice == "see read":
	book_list_readable = open("booklist.txt", "r")
	output = book_list_readable.read()
	print(output)
	no_of_fiction = output.count("fiction")
	no_of_non_fiction = output.count("Non Fiction")
	no_of_books = no_of_fiction + no_of_non_fiction
	print(f"You've read {no_of_fiction} fiction books")
	print(f"You've read {no_of_non_fiction} non fiction books")
	print(f"You've read {no_of_books} books")
else:
	print("Error. Please Try Again")
