import requests

resource_id = "8e8e1b8f-6626-4a0b-93f8-9c99c4340797"
base_url = "https://www.juntadeandalucia.es/datosabiertos/portal/api/3/action/datastore_search"
query = "gimnasio sevilla"
limit = 100
offset = 0
all_records = []

while True:
    params = {
        "resource_id": resource_id,
        "q": query,
        "limit": limit,
        "offset": offset
    }
    response = requests.get(base_url, params=params).json()
    records = response["result"]["records"]
    if not records:
        break
    all_records.extend(records)
    offset += limit

print(f"Total gimnasios encontrados: {len(all_records)}")
