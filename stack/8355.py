def insert_book(shelf, book):
    left, right = 0, len(shelf) - 1
    while left <= right:
        mid = (left + right) // 2
        if shelf[mid] < book:
            left = mid + 1
        else:
            right = mid - 1
    shelf.insert(left, book)

def main():
    shelf = []
    n = int(input())
    for _ in range(n):
        book = int(input())
        insert_book(shelf, book)
    print(*shelf)

if __name__ == "__main__":
    main()
