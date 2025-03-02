import json

# File to store book data
BOOKS_FILE = "books.json"

def load_books():
    """Load books from a JSON file."""
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    """Save books to a JSON file."""
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    """Add a new book to the store."""
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN/Book ID: ")
    genre = input("Enter genre: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity in stock: ")
    
    if not title.isalpha():
        print("Error: Title must be a string.")
        return
    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except ValueError:
        print("Error: Price must be a positive number.")
        return
    try:
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("Error: Quantity must be a non-negative integer.")
        return
    
    for book in books:
        if book["isbn"] == isbn:
            print("Error: A book with this ISBN already exists.")
            return
    
    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "genre": genre,
        "price": price,
        "quantity": quantity
    }
    books.append(new_book)
    save_books(books)
    print("Book added successfully!")

def view_books():
    """Display all books in the store."""
    books = load_books()
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nGenre: {book['genre']}\nPrice: ${book['price']}\nStock: {book['quantity']}\n")

def remove_book():
    """Remove a book by ISBN/Book ID."""
    books = load_books()
    isbn = input("Enter ISBN/Book ID to remove: ")
    
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return
    print("Error: No book found with that ISBN.")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
