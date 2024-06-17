import requests
from bs4 import BeautifulSoup, Comment  # Import Comment from bs4.element
l='< > @ $ db admin password pass administrator user API_KEY http https'.split()
url = input('Enter the site URL: ')
try:
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))  # Find all comments
        print('These are the comments found on the site:')
        for comment in comments:
            found=False
            for i in l:
                if i in comment:
                    found=True
            if found:
                print(comment)
    else:
        print(f'Failed to retrieve content. Status code: {r.status_code}')
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
