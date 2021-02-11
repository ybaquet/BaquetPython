import requests
import dewiki
import json


def request_wikipedia():
    parameters={'action':'query', 'titles':'Chocolatine', 'format':'json', 'prop':'revisions', 'rvprop':'content'}
    r = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    print(dewiki.from_string(r.text))
    if 200 == r.status_code:
        print(r.status_code)
        print(r.text)
        json = r.json()
        query = json['query']
        pages = query['pages']
        for key, value in pages.items():
            p2 = {'action':'query', 'pageids':value['pageid'], 'format':'json'}
            r2 = requests.get('https://en.wikipedia.org/w/api.php?', params=p2)
            jsonD = json.dumps(r2.text)
            jsonL = json.loads(jsonD)

            print(dewiki.from_string(r2.text))
 
if __name__ == '__main__':
    request_wikipedia()