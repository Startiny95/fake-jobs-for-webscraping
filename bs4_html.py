from bs4 import BeautifulSoup
import csv


with open('fake jobs for webscraping/file_1.html', 'r', encoding='utf-8') as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
'''
print("title of page: " , soup.title.name)
print("job title: " , soup.find_all(class_='title is-5'))
print("company name: " , soup.find_all(class_='subtitle is-6'))
print("location: " , soup.find_all(class_='location'))
'''
'''
for a in soup.find_all("h2", class_='title is-5'):
    print("job title: ", a.text)

for a in soup.find_all("h3", class_='subtitle is-6 company'):
    print("company name: ", a.text)

for a in soup.find_all("p", class_='location'):
    print("location: ", a.text)

#print("job title: " , soup.find_all(class_='title is-5'))

for a in soup.find_all(class_='card-footer-item', href=True):
    print("found url: ", a['href'])
'''

for a in soup.find_all(class_= "card"):
    print("job title: ", a.find(class_='title is-5').text.strip())
    print("company name: " , a.find(class_='subtitle is-6 company').text.strip())
    print("location: " , a.find(class_='location').text.strip())
    print("found url: ", a.find(class_='card-footer-item', string = "Apply" ,href=True)['href'])



with open('jobs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["job title","company name","location","found url"])
    for a in soup.find_all(class_= "card"):
        v1 = a.find(class_='title is-5').text.strip()
        v2 = a.find(class_='subtitle is-6 company').text.strip()
        v3 = a.find(class_='location').text.strip()
        v4 = a.find(class_='card-footer-item', string = "Apply" ,href=True)['href']
        writer.writerow([v1, v2, v3, v4])