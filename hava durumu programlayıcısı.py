import requests

def get_weather(city):
    api_key = 'aee9368ab4b3e538bec75d39005eccf3'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    weather_data = response.json()

    sky_description = weather_data['weather'][0]['description']
    city_name = weather_data['name']
    sky_types = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
    sky_types_tr = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    sky_description_tr = next((desc_tr for sky, desc_tr in zip(sky_types, sky_types_tr) if sky == sky_description), sky_description)

    temp = round((weather_data['main']['temp'] - 273.15), 2)
    feels_temp = round((weather_data['main']['feels_like'] - 273.15), 2)
    temp_min = round((weather_data['main']['temp_min'] - 273.15), 2)
    temp_max = round((weather_data['main']['temp_max'] - 273.15), 2)

    weather_summary = {
        "Şehir": city_name,
        "Gökyüzü": sky_description_tr,
        "Sıcaklık": temp,
        "Hissedilen": feels_temp,
        "Minimum": temp_min,
        "Maksimum": temp_max
    }

    return weather_summary


if __name__ == "__main__":
    sehir_ismi = "İstanbul"
    print(get_weather(sehir_ismi))
