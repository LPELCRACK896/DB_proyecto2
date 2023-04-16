from faker import Faker
import json

# Initialize Faker instance
fake = Faker()
count = 0
games = []

# Generate fake video game data
while count < 1000:
    game = {
        "row_key": fake.uuid4(),
        "game_info:game_name": fake.word(),
        "game_info:genre": fake.word(),
        "game_info:platform": fake.random_element(elements=('PC', 'PS4', 'Xbox One', 'Nintendo Switch')),
        "game_info:release_year": fake.random_int(min=2000, max=2023),
        "game_info:developer": fake.company(),
        "game_info:price": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    }
    games.append(game)
    count += 1

# Create JSON document from video game data with indentation
with open("games.json", "w") as f:
    json.dump(games, f, indent=4)

# Print a message to confirm that the file was written
print("Data written to games.json")
