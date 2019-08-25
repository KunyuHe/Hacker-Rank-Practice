# Enter your code here. Read input from STDIN. Print output to STDOUT

def take_input():
    try:
        query = str(input())
    except:
        query = None

    return query


t = int(input())
phone_book = dict()

for i in range(t):
    name, phone_number = str(input()).split()
    phone_book[name] = phone_number

query = take_input()
while query:
    phone_number = phone_book.get(query, None)
    if not phone_number:
        print("Not found")
    else:
        print("{}={}".format(query, phone_number))
    query = take_input()
