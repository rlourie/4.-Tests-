import requests


def upload(file_path: str, token):
    link = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = token
    params = {
        "path": file_path,
        "overwrite": "true"
    }
    headers = {
        'Content_Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }

    response = requests.put(link, params=params, headers=headers)
    try:
        response.raise_for_status()
        return response.status_code
    except Exception:
        return response.status_code


file_path = ''
token = '********'
