
books = {}
for _ in range(int(input())):
    book = input()
    if book in books.keys():
        books[book] = books.get(book) + 1
    else:
        books[book] = 1

max(books, key=books.get)
result = [k for k, v in books.items() if max(books.values()) == v]
result.sort()
print(result[0])
