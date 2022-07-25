"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
"""
def city_country(city, country):
    print(city.title() + ", " + country.title())

city_countries = dict()
city_countries['Singapore'] = 'singapore'
city_countries['Las Vegas'] = 'united states of america'
city_countries['Boston'] = 'united states of america'

for city, country in city_countries.items():
    city_country(city, country)

"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
"""

def make_album(artist_name, album_title, number_of_tracks =''):
    album_dictionary = dict()
    album_dictionary['artist_name'] = artist_name
    album_dictionary['album_title'] = album_title
    if number_of_tracks != '':
        album_dictionary['number_of_tracks'] = number_of_tracks
    return album_dictionary

print(make_album('Joey Badass', '2000'))
print(make_album('Future', 'High on Life'))
print(make_album('Pusha T', 'Daytona'))
print(make_album('Rakim', 'Paid in Full', 20))

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop
"""
artists_album_message = "Please enter an artist: "
title_message = "Please enter the title: "
quit_message = "Do you want to stop input? Enter quit to exit: "
while True:
    artist = input(artists_album_message)
    title = input(title_message)
    print(make_album(artist_name=artist, album_title=title))
    
    quit = input(quit_message)
    if quit == 'quit':
        break

