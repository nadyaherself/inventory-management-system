import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Y008gb7TY&4",
    database = "inventory_system"
)
cursor = conn.cursor()

def add_item():
    name = input("Item Name    : ")
    code = input("Item Code    : ")
    quantity = int(input("Quantity  : "))
    price = float(input("Price  :" ))
    category = input("Category  : ")

    sql = "INSERT INTO inventory (item_name, item_code, quantity, price, category) VALUES (%s, %s, %s, %s, %s)"
    val = (name, code, quantity, price, category)
    cursor.execute(sql, val)
    conn.commit()
    print (cursor.rowcount, "item added.")

def view_items():
    cursor.execute("SELECT * FROM inventory")
    result = cursor.fetchall()
    for row in result:
        print(row)
def update_item():
    item_id = input("Enter Item ID to update    : ")
    quantity = int(input("New Quantity  : "))
    price = float(input("New Price  : "))

    sql = "UPDATE inventory SET quantitiy = %s, price = %s WHERE item_id = %s"
    val = (quantity, price, item_id)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "item updated.")

def delete_item():
    item_id = input("Enter Item ID to delete    : ")
    sql = "DELETE FROM inventory WHERE item_id = %s"
    val = (item_id,)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "item deleted.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

main()
cursor.close()
conn.close()