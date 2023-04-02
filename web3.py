import requests
import webbrowser
from bs4 import BeautifulSoup

URL = 'https://curiouspumpkincom.wordpress.com/blog/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('h2',class_='entry-title')

num = 1
for i in results:
    title = i.find('a').text
    print(num, ":", title)
    num += 1

while True:
    choice = input("Enter the number of the blog post you want to open (or 'q' to quit): ")
    if choice == 'q':
        break
    elif not choice.isnumeric() or int(choice) not in range(1, num):
        print("Invalid input. Please enter a number or 'q' to quit.")
    else:
        Blog_post = results[int(choice)-1].find('a').text
        url = results[int(choice)-1].find('a')['href']
        print("Opening:", Blog_post)
        webbrowser.open(url)
