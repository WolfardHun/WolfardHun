from faker import Faker
import json
import os
import subprocess
from datetime import datetime

# Faker inicializálása
fake = Faker()

# Adatok generálása
def generate_data():
    data = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "company": fake.company(),
        "job": fake.job(),
        "timestamp": datetime.now().isoformat()
    }
    return data

# Adatok mentése JSON fájlba
def save_data_to_file(data):
    with open("data.json", "a") as file:
        file.write(json.dumps(data) + "\n")

# Adatok feltöltése GitHubra
def push_to_github():
    try:
        # Git parancsok futtatása
        subprocess.run(["git", "add", "data.json"], check=True)
        subprocess.run(["git", "commit", "-m", "Új adat generálva"], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Git hiba: {e}")

    print("Új adat generálva és feltöltve.")

# Script futtatása
if __name__ == "__main__":
    generated_data = generate_data()
    save_data_to_file(generated_data)
    push_to_github()
    print("Új adat generálva és feltöltve.")
