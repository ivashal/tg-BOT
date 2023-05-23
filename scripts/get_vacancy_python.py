import requests
from random import randint, sample

def get_random_vacancy():
    URL: str = 'https://api.hh.ru/vacancies?'

    headers: dict = {
        'User-Agent': 'api-test-agent'
    }
    params: dict = {
        'page': '1',        # страница
        'per_page': '100',  # количество результатов на странице
        'text': 'python',   # встречается в тексте
        'area': '2'         # область Санкт-Петербург
    }

    ids: list = [str]   #список для id вакансий
    resp = requests.get(URL, headers=headers, params=params)
    data = resp.json()
    count_page = data['pages']  # количество страниц с результатами
    count_id = data['found']    # всего вакансий найдено

    for i in range(count_page + 1):
        resp = requests.get(f'https://api.hh.ru/vacancies?page={i}&per_page=100&text=python&area=2')
        data = resp.json()
        for item in data['items']:
            ids.append(item['id'])
    print(f'found ids = {count_id}, parsed ids = {len(ids)}')

    rand_ids = sample(ids, 3)
    list_of_data_vacancy: list = [dict]

    for id in rand_ids:
        url_rand_vacancies = f'https://api.hh.ru/vacancies/{id}'
        resp_vacancies = requests.get(url=url_rand_vacancies, headers=headers).json()
        data_vacancy = {'name': resp_vacancies["name"],
                        'created_at': resp_vacancies["created_at"],
                        'salary': resp_vacancies["salary"],
                        'url': resp_vacancies["alternate_url"]
                        }
  
        list_of_data_vacancy.append(data_vacancy.copy())


    return list_of_data_vacancy

print(get_random_vacancy())
