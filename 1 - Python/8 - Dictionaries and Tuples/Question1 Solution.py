stock = {
    "Meat":140,
    "Veggie":270,
    "Fruits":368,
    "JunkFood":740
    }

def show():
    for product,s in stock.items():
        print(f"{product} -> {s}")

def add():
    show()
    product = input("Enter Product Name to Add : ")
    product = product.capitalize()
    if product in stock:
        print(f'{product} Already Exist In Our Dataset. Terminating')
        return
    s = input(f"Enter Stock Value for {product} : ")
    s = int(s)
    stock[product]= s   #Adds New Key Value Pair to Dictionary
    show()

def remove():
    show()
    product = input("Enter Product Name to Remove : ")
    product = product.capitalize()
    if product not in stock:
        print(f"{product} Doesn't Exist In Our Dataset. Terminating")
        return
    stock.pop(product)
    show()

def main():
    choice = input("Enter Operation (add,remove,show) : ")
    if choice.lower() == 'add':
        add()
    elif choice.lower() == 'remove':
        remove()
    elif choice.lower() == 'show':
        show()

if __name__ == '__main__':
    main()
