import requests                        
from bs4 import BeautifulSoup           
from fake_useragent import UserAgent    


def get_weather_spb() -> list:
    ua = UserAgent()
    URL: str = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
        
    response = requests.get(URL, headers={'User-agent': ua.random})
    html: str = response.text
        
    soup = BeautifulSoup(html, 'html.parser')
    date: str = soup.find('div', 'dates short-d').text
    table_weather_today = soup.find('table', 'weather-today short')
    rows_table_today = table_weather_today.find_all(name='tr')
    weather_day_list: list = []

    for row in rows_table_today:
        info_weather: dict = {}
        info_weather['weather_day'] = row.find('td', 'weather-day').text
        info_weather['temperature'] = row.find('td', 'weather-temperature').text
        info_weather['tooltip'] = row.find('div')['title']
        info_weather['weather-feeling'] = row.find('td', 'weather-feeling').text
        info_weather['weather-humidity'] = row.find('td', 'weather-humidity').text
        weather_day_list.append(info_weather)

    weather_day_list.insert(0, date)

    return weather_day_list

for item in get_weather_spb():
    print(item)
