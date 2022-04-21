with open('planets.txt', 'w', encoding='utf-8') as file:
  planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
  for planet in planets:
    file.write(planet + '\n')
