import requests
import time


with open('key.txt', 'r') as myfile:
    API_KEY = myfile.read()
API_URL = 'https://api.esv.org/v3/passage/text/'


def get_esv_text(passage):
    time.sleep(1)  # Not allowed to make more than 60 queries per second

    params = {
        'q': passage,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)
    passages = response.json()['passages']
    return passages[0].strip() if passages else 'Error: Passage not found'


if __name__ == '__main__':
    with open('output.txt', 'w+') as file_out:
        with open('input.txt', 'r') as file_in:
            for line_number, line_contents in enumerate(file_in):
                this_verse = get_esv_text(line_contents) + ' - ' + line_contents
                file_out.write(this_verse + '\n')
                print(this_verse)
