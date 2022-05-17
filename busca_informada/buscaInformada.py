import geopy.distance

coords_1 = (-9.660130, -35.700980)
coords_2 = (-9.769090749124917, -35.84067567217628)

def getDistance(c1, c2):
  distanceStr = str(geopy.distance.distance(c1, c2)).split(' ')[0]
  distance = round(float(distanceStr), 2)
  return distance

print(getDistance(coords_1, coords_2))

# Coordenadas dos Estados / Renomeadas para Cidade - Heurística
statesLatLong = {
    "Rio Branco": [-8.77, -70.55],
    "Maceió": [ -9.71, -35.73],
    "Manaus": [ -3.07, -61.66],
    "Macapá": [  1.41, -51.77],
    "Salvador": [-12.96, -38.51],
    "Fortaleza": [ -3.71, -38.54],
    "Brasília": [-15.83, -47.86],
    "Vitória": [-19.19, -40.34],
    "Goiânia": [-16.64, -49.31],
    "São Luís": [ -2.55, -44.30],
    "Cuiabá": [-12.64, -55.42],
    "Campo Grande": [-20.51, -54.54],
    "Belo Horizonte": [-18.10, -44.38],
    "Belém": [ -5.53, -52.29],
    "João Pessoas": [ -7.06, -35.55],
    "Curitiba": [-24.89, -51.55],
    "Recife": [ -8.28, -35.07],
    "Teresina": [ -8.28, -43.68],
    "Rio de Janeiro": [-22.84, -43.15],
    "Natal": [ -5.22, -36.52],
    "Porto Velho": [-11.22, -62.80],
    "Porto Alegre": [-30.01, -51.22],
    "Boa Vista": [  1.89, -61.22],
    "Florianópolis": [-27.33, -49.44],
    "Aracaju": [-10.90, -37.07],
    "São Paulo": [-23.55, -46.64],
    "Palmas": [-10.25, -48.25],
}

def getCityLatLong(city):
  return statesLatLong[city]

print(getCityLatLong('Maceió'))