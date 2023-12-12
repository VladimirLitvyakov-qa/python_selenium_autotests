import requests
import pytest

HOST = "https://api.pokemonbattle.me:9104"
my_trainer_id = "3850"

def test_status_code():
    response = requests.get(url=f"{HOST}/trainers")
    assert response.status_code == 200

def test_check_trainer():
    response = requests.get(url=f"{HOST}/trainers", params={"trainer_id": my_trainer_id})
    trainer_data = response.json()
    assert trainer_data.get('id') == my_trainer_id