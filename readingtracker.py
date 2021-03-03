book_list = open("booklist.txt", "a")
choice = input("add new or see read ").lower()
if choice == "add new":
	book_name = input("book name: ")
	author_name = input("author name: ")
	fiction_or_non_fiction = input("fiction or non fiction ").lower()
	book_rating = input("rate the book: ")
	book_list.write(f"{book_name}, {author_name}, {fiction_or_non_fiction}, {book_rating}," + "/10" + "\n")
	print(f"{book_name} has been added to your booklist")
elif choice == "see read":
	book_list_readable = open("booklist.txt", "r")
	output = book_list_readable.read()
	print(output)
	no_of_fiction = output.count("fiction")
	no_of_non_fiction = output.count("non-fiction")
	print(f"You've read {no_of_fiction} fiction books")
	print(f"You've read {no_of_non_fiction} non fiction books")
else:
	print("Error. Please Try Again")
