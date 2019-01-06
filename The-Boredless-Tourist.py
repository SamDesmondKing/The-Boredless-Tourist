# -- The Boredless Tourist --
#
# Tourism recommendation engine built for CodeCademy.
# My first Python program.
#

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):

  destination_index = destinations.index(destination)
  return destination_index


print(get_destination_index('Paris, France'))
