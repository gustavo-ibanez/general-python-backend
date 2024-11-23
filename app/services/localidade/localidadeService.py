from flask import current_app

class LocalidadeService:

    def __init__(self):
        pass

    def requestLocation(self):
        return [
            {
                "_id": "BR",
                "name": "Brasil",
                "state": {
                        "AC": "Acre",
                        "AL": "Alagoas",
                        "AP": "Amapá",
                        "BA": "Bahia",
                        "CE": "Ceará",
                        "DF": "Distrito Federal",
                        "ES": "Espírito Santo",
                        "GO": "Goiás",
                        "MA": "Maranhão",
                        "MT": "Mato Grosso",
                        "MS": "Mato Grosso do Sul",
                        "MG": "Minas Gerais",
                        "PA": "Pará",
                        "PB": "Paraíba",
                        "PR": "Paraná",
                        "PE": "Pernambuco",
                        "PI": "Piauí",
                        "RJ": "Rio de Janeiro",
                        "RN": "Rio Grande do Norte",
                        "RS": "Rio Grande do Sul",
                        "RO": "Rondônia",
                        "RR": "Roraima",
                        "SC": "Santa Catarina",
                        "SP": "São Paulo",
                        "SE": "Sergipe",
                        "TO": "Tocantins"
                }
            },
            {
                "_id": "CA",
                "name": "Canadá",
                "state": {
                    "AB": "Alberta",
                    "BC": "British Columbia",
                    "MB": "Manitoba",
                    "NB": "New Brunswick",
                    "NL": "Newfoundland and Labrador",
                    "NS": "Nova Scotia",
                    "ON": "Ontario",
                    "PE": "Prince Edward Island",
                    "QC": "Quebec",
                    "SK": "Saskatchewan",
                    "NT": "Northwest Territories",
                    "NU": "Nunavut",
                    "YT": "Yukon"
                }
            },
            {
                "_id": "US",
                "name": "United States",
                "state": {
                        "AL": "Alabama",
                        "AK": "Alaska",
                        "AZ": "Arizona",
                        "AR": "Arkansas",
                        "CA": "California",
                        "CO": "Colorado",
                        "CT": "Connecticut",
                        "DE": "Delaware",
                        "FL": "Florida",
                        "GA": "Georgia",
                        "HI": "Hawaii",
                        "ID": "Idaho",
                        "IL": "Illinois",
                        "IN": "Indiana",
                        "IA": "Iowa",
                        "KS": "Kansas",
                        "KY": "Kentucky",
                        "LA": "Louisiana",
                        "ME": "Maine",
                        "MD": "Maryland",
                        "MA": "Massachusetts",
                        "MI": "Michigan",
                        "MN": "Minnesota",
                        "MS": "Mississippi",
                        "MO": "Missouri",
                        "MT": "Montana",
                        "NE": "Nebraska",
                        "NV": "Nevada",
                        "NH": "New Hampshire",
                        "NJ": "New Jersey",
                        "NM": "New Mexico",
                        "NY": "New York",
                        "NC": "North Carolina",
                        "ND": "North Dakota",
                        "OH": "Ohio",
                        "OK": "Oklahoma",
                        "OR": "Oregon",
                        "PA": "Pennsylvania",
                        "RI": "Rhode Island",
                        "SC": "South Carolina",
                        "SD": "South Dakota",
                        "TN": "Tennessee",
                        "TX": "Texas",
                        "UT": "Utah",
                        "VT": "Vermont",
                        "VA": "Virginia",
                        "WA": "Washington",
                        "WV": "West Virginia",
                        "WI": "Wisconsin",
                        "WY": "Wyoming"
                }
            }
        ];
