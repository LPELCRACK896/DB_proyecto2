from faker import Faker
import json
import os

current_dir = os.path.abspath(os.getcwd())
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)

def gen_purchase(filename, total = 100):
    fake = Faker()
    count = 0
    lista = []

    # Generate fake purchase data
    while count < total:
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
        count += 1
        lista.append(purchase_data)

    # Create JSON document from purchase data with indentation
    with open(f"{dir_path}/{filename}", "w") as f:
        json.dump(lista, f, indent=4)

    # Print a message to confirm that the file was written
    print(f"Data written to {filename}")

def gen_games(filename, total = 100):
    # Initialize Faker instance
    fake = Faker()
    games = []
    count = 0

    # Generate fake video game data
    while count < total:
        game = {
            
            "game_info:developer": fake.company(),
            "game_info:price": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        }
        game = {
            fake.random_int(min=1000, max=9999): {
                'game info': {
                    'Name': fake.word(),
                    'Genre': fake.word(),
                    'Plataform': fake.random_element(elements=('PC', 'PS4', 'Xbox One', 'Nintendo Switch')),
                    'Release_year': fake.random_int(min=2000, max=2023),
                    "price": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
                },
                'Dev info': {
                    'Company': fake.company(),
                    'Workers': fake.random_int(min=1000, max=9999),
                },
                'product info': {
                    'Product ID': fake.random_int(min=1000, max=9999, step=1),
                    'Product description': fake.sentence(nb_words=10),
                }
            },
        }
        games.append(game)
        count += 1

    # Create JSON document from video game data with indentation
    with open(f"{dir_path}/{filename}", "w") as f:
        json.dump(games, f, indent=4)

    # Print a message to confirm that the file was written
    print(f"Data written to {filename}")

if __name__ == "__main__":
    gen_games("games.json", 10)
    gen_purchase("purchases.json", 5)