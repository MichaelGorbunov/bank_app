# Функция, которую мы хотим протестировать
def fetch_data(api_client, url):
    response = api_client.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
