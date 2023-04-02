from bs4 import BeautifulSoup
import requests
import webbrowser

URL = 'https://curiouspumpkincom.wordpress.com/blog/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)


results = soup.find_all('h2',class_='entry-title')
print(results)

num = 1
for i in results:
    title = i.find('a').text
    print(num, ":", title)
    num += 1

Blog_post=input("Enter the title of your page: ")

if Blog_post in title_url:
    webbrowser.open(title_url[Blog_post])
else:
    print("Invalid title. Please try again.")