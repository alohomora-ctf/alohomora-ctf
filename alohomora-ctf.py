import random
import string
import time

aws_access_key_id = "QUtJQTVGQ0Q2TUNHV0xGTUdZNFY="
aws_secret_access_key = "aVpKemcxWGhjcEdReFFqY2w1TXJhOS91ZVpCOEN3MTZPR0NXL2ZzbQ=="

def generate_random_string(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for i in range(length))
    return random_string

def simulate_file_download():
    print("Simulating file download...")
    time.sleep(random.uniform(1, 3))
    print("File download complete.")

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def reverse_string(input_string):
    return input_string[::-1]

def simulate_api_call():
    print("Simulating API call...")
    time.sleep(random.uniform(1, 2))
    response = {"status": "success", "message": "Data retrieved"}
    return response

def perform_operations():
    random_string = generate_random_string(12)
    print(f"Generated Random String: {random_string}")

    random_number = generate_random_number(1, 100)
    print(f"Random Number between 1 and 100: {random_number}")

    reversed_string = reverse_string(random_string)
    print(f"Reversed String: {reversed_string}")

    simulate_file_download()

    api_response = simulate_api_call()
    print(f"API Response: {api_response}")

perform_operations()
