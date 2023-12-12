import requests

HOST = "https://api.pokemonbattle.me:9104"

response = requests.post(url=f"{HOST}/pokemons",
                        headers={"Content-Type": "application/json", "trainer_token": "9aaf493e2ebf489a59b27e8384862a90"},
                        json={"name": "generate",
                              "photo": "generate"},
                        timeout=5
                        )
print(f"Message: {response.text}")

response = requests.put(url=f"{HOST}/pokemons",
                        headers={"Content-Type": "application/json", "trainer_token": "9aaf493e2ebf489a59b27e8384862a90"},
                        json={"pokemon_id": "19880",
                              "name": "Barashik"},
                        timeout=5
                        )
print(f"Message: {response.text}")

response = requests.post(url=f"{HOST}/trainers/add_pokeball",
                        headers={"Content-Type": "application/json", "trainer_token": "9aaf493e2ebf489a59b27e8384862a90"},
                        json={"pokemon_id": "19880"},
                        timeout=5
                        )
print(f"Message: {response.text}")