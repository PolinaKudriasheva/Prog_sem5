import requests

api_key = "0b0c090d4c1c6cfe432a2af8e4c5aa56" # api ключ 
url = "http://api.openweathermap.org/data/2.5/weather" # урл запроса

def get_weather_data(place, key=api_key):

    res = requests.get( # отправка запроса
        url,
        params = { # объвляение параметров
            "q": place,
            "appid": key,
            "units": "metric" # возвращать градусы в цельсиях
        }

    )

    return res.text # парсинг в текст и возврат из функции
    
    
if __name__ == "__main__":
    print(get_weather_data("Saint Petersburg"))
    print(get_weather_data("Moscow"))
    print(get_weather_data("Dhaka"))
