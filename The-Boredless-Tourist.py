# -- The Boredless Tourist --------------------------
#
# Tourism recommendation engine built for CodeCademy.
# My first Python program.
#
# ---------------------------------------------------

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = []
for entry in destinations:
  attractions.append([])

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
  except ValueError:
    return

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["the Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  attractions_with_interest = []
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]

  for results in attractions_in_city:
    possible_attraction = []
    attraction_tags = []
    possible_attraction += results
    attraction_tags += results[1]
    for each_interest in interests:
      if each_interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  loop_count = 0

  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi "+str(traveler[0])+", we think you'll like these places around "+traveler_destination+": "

  for attraction in traveler_attractions:
    interests_string += attraction
    loop_count += 1
    if loop_count < len(traveler_attractions):
      interests_string += ", "
    else:
      interests_string += "."

  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)

