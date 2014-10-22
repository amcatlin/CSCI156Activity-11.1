__author__ = 'Alicia'

actorchar = {'Johnny Depp': ['Mad Hatter', 'Sweeny Todd', 'Captin Jack Sparrow', 'Edward Scissorhands'],  #1
             'Geena Davis': ['Dottie Hinson', 'Barbara Maitland', 'Thelma'],
             'Kathy Bates': ['Annie Wilkes', 'Evelyn Couch', 'Dolores Claiborne', 'Molly Brown'],
             'Jack Nicholson': ['Jack Torrance', 'Joker/Jack Napier' , 'Col. Nathan R. Jessup'],
             'Robert De Niro': ['Sam Rothstein', 'David Callaway', 'Jack Byrnes', 'Young Vito Corleone']}

print(actorchar['Kathy Bates'])  #2
print(actorchar.get('Jack Nicholson'))  #3

for key in actorchar:  #4
    print(actorchar[key])


for key in actorchar:  #5
    if key == 'pie':
        print('I like pie')
    else:
        print(actorchar[key])
