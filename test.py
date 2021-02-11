import pkg_resources, os, time
import requests

for package in pkg_resources.working_set:
#    print("%s: %s" % (package, time.ctime(os.path.getctime(package.location))))
    print(str(package) + ": " +str(package.location))
    
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'titles': 'Chocolatine',
        'format': 'json',
    }).json()
https://fr.wikipedia.org/w/api.php?action=query&titles=pain_au_chocolat&prop=revisions&rvprop=content&format=json