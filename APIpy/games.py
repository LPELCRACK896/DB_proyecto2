from faker import Faker
import json

# Initialize Faker instance
fake = Faker()
count = 0
games = []

# Generate fake video game data
while count < 1000:
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
with open("games.json", "w") as f:
    json.dump(games, f, indent=4)

# Print a message to confirm that the file was written
print("Data written to games.json")
