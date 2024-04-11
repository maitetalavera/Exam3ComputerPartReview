###############################################################################
# TODO: 1.
#
#   For this module, we are going to create a basic library catalog. For our
#   purposes, a book is going to be defined as a dictionary with these keys:
#       - isbn
#       - title
#       - author
#       - publisher
#       - checked_out
#
#   For this __todo__, write a function called print_books that takes one
#   argument:
#       - books     <-- list of dictionaries (books)
#
#   First, it should print the line:
#       Books:
#   
#   Then, This function should loop through the list of books and, for each
#   book, print information about the book like so:
#
#       ISBN: 978-0679203735
#       Title: 20,000 Leagues Under the Sea
#       Author: Jules Verne
#       Publisher: Random House Childrens Books
#
#   Notice that checked_out is NOT printed.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def print_books(books):
    print("\nbooks:")
    for book in books:
        if book ["checked out"] == False:
            print(f'"ISBN')
        

###############################################################################
# TODO: 2.
#
#   For this _todo_, write a function called checkout() that takes one
#   parameter:
#       - book      <-- dictionary (book)
#
#   This function should behave like this:
#
#       - If the book's checked_out value is False (that is, it is not checked
#         out), it should set the value of checked_out to True and print:
#           "Successfully Checked Out <BOOK TITLE HERE>!"
#       - If the book's checked_out value is True (that is, it is checked out),
#         it should print:
#           "Book Already Checked Out"
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def checkout(book):
    if book["checked_out"] == False:
        book["checkedout]"] = True
        print()

    else:
        print()

###############################################################################
# TODO: 3.
#
#   Now, let's create our library catalog system.
#
#   For this _todo_, write a function called main() that will start things off.
#   This function should do these things in order:
#
#       1. Print a welcome message to the user
#       2. Continually ask the user for information about books (isbn, title,
#          author, publisher). If the user types "end" for any of the fields,
#          the program should stop asking for book information. (HINT: I used a
#          while loop)
#       3. For each book, create a dictionary to hold the book's information.
#          The dictionary should have all of this information: isbn, title,
#          author, publisher, checked_out. The checked_out key should have the
#          value False to begin with.
#       4. It should keep track of all the books in a list.
#       5. Once the user stops entering book information, the program should
#          use the print_books() method to print the list of books and their
#          information.
#       6. Then, the program should continually prompt the user like so:
#           "Which book would you like to check out? "
#       7. If the user types a book title that is in the list of books, it
#          should "checkout" the book (using the checkout() method) and reprint
#          the list of books. It should keep asking the user for more books to
#          check out until they type "end" 
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def main():
    print("Welcome")
   
    books = []

    while True :
        isbn = input ("Please enter")
        if isbn == "end" : break 
        title = input ("Please enter")
        if title == "end" : break 
        author = input ("Please enter")
        if author == "end" : break 
        publisher = input ("Please enter")
        if publisher == "end" : break 

        book = {
            "isbn" : isbn, 
            "title": title,
            "author":author,
        }
        books.appen(book)
    print_books(books)
        while Truee: 
            checkout_entry = input("which book")
            if checkout_entry == "end":break