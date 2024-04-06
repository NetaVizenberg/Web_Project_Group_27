from mongodrafts import products_col, user_col

#Find documents in the products collection
products = products_col.find()
print("Products Collection:")
for product in products:
    print(product)

#Find documents in the user collection
users = user_col.find()
print("\nUser Collection:")
for user in users:
    print(user)
