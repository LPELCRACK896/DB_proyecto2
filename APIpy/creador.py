from faker import Faker
import json

# Initialize Faker instance
fake = Faker()
count = 0
lista=[]

# Generate fake purchase data
while count <= 1000:
    purchase_data = {
        fake.random_int(min=1000, max=9999): {
            'customer info': {
                'Name': fake.name(),
                'Age': fake.random_int(min=18, max=80, step=1),
                'Address': fake.address(),
                'Email': fake.email(),
                'Phone Number': fake.phone_number(),
            },
            'purchase info': {
                'Date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
                'Time': fake.time(),
                'Total Price': fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                'Payment Type': fake.random_element(elements=('Credit Card', 'Debit Card', 'Cash')),
            },
            'product info': {
                'Product ID': fake.random_int(min=1000, max=9999, step=1),
                'Product Name': fake.word(),
                'Quantity': fake.random_int(min=1, max=10, step=1),
            }
        },
    }
    count +=1
    lista.append(purchase_data)

# Create JSON document from purchase data with indentation
with open("purchases.json", "w") as f:
    json.dump(lista, f, indent=4)

# Print a message to confirm that the file was written
print("Data written to data.json")
