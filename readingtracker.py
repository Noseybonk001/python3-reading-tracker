book_list = open("booklist.txt", "a")
choice = input("add new or see read ").lower()
if choice == "add new":
	book_name = input("book name: ")
	author_name = input("author name: ")
	book_rating = input("rate the book: ")
	book_list.write(f"{book_name}, {author_name}, {book_rating}" +"/10" + "\n")
	print(f"{book_name} has been added to your booklist")
elif choice == "see read":
	book_list_readable = open("booklist.txt", "r")
	output = book_list_readable.read()
	print(output)
else:
	print("Error. Please Try Again")	
