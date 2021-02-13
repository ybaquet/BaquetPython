import requests
import dewiki
import json


def request_wikipedia(title, filename=None, loop=0):
    try:
        title = title.strip().lower()
        while '  ' in title:
            title = title.replace('  ', ' ')
        parameters = {'action':'query', 'titles':title, 'format':'json', 'prop':'revisions', 'rvslots':'*', 'rvprop':'timestamp|user|comment|content'}
        r = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
        json = r.json()
        query = json['query']
        pages = query['pages']
        page = list(pages.values())[0]
        revisions = page['revisions']
        revision = revisions[0]
        slots = revision['slots']
        slot = slots['main']
        text = slot['*']
        text = dewiki.from_string(text)
        if None == filename:
            filename = title+".wiki"
        if 0 == loop and text.startswith("#REDIRECT"):
            request_wikipedia(text[9:], filename, 1)
        else:
            if ('}}\n') in text:
                text = text[text.index('}}\n') + 3 :]
            out = open(filename, "w")
            out.write(text)
    except (KeyError, IndexError):
        print('No page found for "' + title + '"!')
 
if __name__ == '__main__':
    request_wikipedia("paIn   au   chOcolat")
    request_wikipedia("chocolatine")
    request_wikipedia("Chocolatine")
    request_wikipedia("dsl---;'dfgl")

