import requests

print(requests.get('http://google.com').text)
url='https://raw.githubusercontent.com/FrankQixin/lab1/master/script_2.py'
r=requests.get(url).text
print(r)
with open ('script_3.py','w') as doc:
    doc.write(r)
    doc.close()
