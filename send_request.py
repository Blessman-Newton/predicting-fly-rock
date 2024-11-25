import requests
import json

url = 'http://localhost:5000/predict'

# %%
data = [
    {
        "burden": 1.0,
        "spacing": 2.0,
        "ucs": 3.0,
        "bench_height": 4.0,
        "hole_diameter": 5.0,
        "initial_stemming_height_": 6.0,
        "final_stemming_height": 7.0,
        "charge_length": 8.0,
        "charge_hole_": 9.0,
        "powder_factor": 10.0
    }
]

# Convert the data to JSON format
json_data = json.dumps(data)
json_data

# %%
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json_data)


# %%
print(response.json())

# %%



