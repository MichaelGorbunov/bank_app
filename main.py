import requests


def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    data = response.json()
    result = {}
    result['name'] = data.get('name')
    result['language'] = data.get('language')
    result['forks'] = data.get('forks_count')
    result['stars'] = data.get('stargazers_count')

    if None in result.values():
        return None

    return result


if __name__ == '__main__':
    URL = 'https://api.github.com/repos/ArjanCodes/betterpython'
    repo_info = get_data(URL)
    print(repo_info)