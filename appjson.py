from Utils import databasejson

USER_CHOICE = """
Enter
    'a' - Add a book
    'r' - Mark a book as read
    'd' - Delete a book
    'l' - List the books
    'q' - Quit 
Your Choice : """

def menu():
    databasejson.create_file_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            delete_book()
        elif user_input == 'l':
            list_book()
        else:
            print('Unknown command, Please try again')
        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name :')
    author = input ('Enter the author name :')
    databasejson.add_book(name,author)

def list_book():
    books = databasejson.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] == True else 'No'
        print (f"Book name {book['name']}  by {book['author']} and read: {read}" )

def prompt_read_book():
    name = input('Input the name of the book you read:')
    databasejson.mark_book_as_read(name)

def delete_book():
    name = input('Input the book name to delete :')
    databasejson.delete_book(name)

menu()

