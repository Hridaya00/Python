
b = {101: "Python", 102: "Data Structures", 103: "AI", 104: "Machine Learning"}
a = {101, 102, 103, 104}
r = []
c = {}

def borrow(s, i):
    if i not in b:
        print("book does not exist")
    elif i not in a:
        print("book unavailable")
    else:
        a.remove(i)
        r.append((s, i, "borrowed"))
        if s in c:
            c[s] += 1
        else: 
            c[s] = 1
        print("book borrowed successfully")

def ret(s, i):
    if i not in b:
        print("book does not exist")
    elif i in a:
        print("book not borrowed")
    else:
        a.add(i)
        r.append((s, i, "returned"))
        print("book returned successfully")

def show():
    print("available books:")
    for i in a:
        print(i, b[i])

    print("borrowed books:")
    for i in b:
        if i not in a:
            print(i, b[i])

while True:
    print("\n1.Borrow")
    print("2.Return")
    print("3.Show books")
    print("4.Show records")
    print("5.Show counts")
    print("6.Exit")

    x = input("Enter choice: ")

    if x == "1":
        s = input("Student ID: ")
        i = int(input("Book ID: "))
        borrow(s, i)

    elif x == "2":
        s = input("Student ID: ")
        i = int(input("Book ID: "))
        ret(s, i)

    elif x == "3":
        show()

    elif x == "4":
        print(r)

    elif x == "5":
        print(c)

    elif x == "6":
        print("Returning to terminal..........")
        break

    else:
        print("Invalid choice")