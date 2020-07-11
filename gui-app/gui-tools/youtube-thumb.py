import requests #pip install requests
template = 'https://img.youtube.com/vi/{}/0.jpg'
link1 = str(input('Enter Youtube Link : '))
a,b = link1.split('=')

new = template.format(b)
data = requests.get(new).content
with open('thumbnail.jpg','wb') as file:
    file.write(data)