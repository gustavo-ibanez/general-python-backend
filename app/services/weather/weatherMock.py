from .weather import Weather

class WeatherMock(Weather):

    def callLocation(self, city, stateCode, countryCode):
        return [{
                    "name":"Presidente Prudente",
                    "local_names":{
                        "pt":"Presidente Prudente"
                    },
                    "lat":-22.1225167,
                    "lon":-51.3882528,
                    "country":"BR",
                    "state":"São Paulo"
                }]

    def callWeather(self, lat, lon):
        return {
                    "coord":{
                        "lon":-51.3883,
                        "lat":-22.1225
                    },
                    "weather":[
                        {
                            "id":801,
                            "main":"Clouds",
                            "description":"algumas nuvens",
                            "icon":"02d"
                        }
                    ],
                    "base":"stations",
                    "main":{
                        "temp":24.81,
                        "feels_like":25.25,
                        "temp_min":24.81,
                        "temp_max":24.81,
                        "pressure":1014,
                        "humidity":73,
                        "sea_level":1014,
                        "grnd_level":965
                    },
                    "visibility":10000,
                    "wind":{
                        "speed":4.12,
                        "deg":150
                    },
                    "clouds":{
                        "all":20
                    },
                    "dt":1730140214,
                    "sys":{
                        "type":1,
                        "id":8355,
                        "country":"BR",
                        "sunrise":1730105006,
                        "sunset":1730151298
                    },
                    "timezone":-10800,
                    "id":3452324,
                    "name":"Presidente Prudente",
                    "cod":200
                }