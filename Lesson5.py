# f = open('text.txt', 'w')
# f.write("Hallo world")
# f.close()
#
# # f1=open("text2.txt", "w")
# # f1.write("Hall world, I'm here" '\n')
# # f1.close()
# # f1=open("text2.txt",'r')
# # m=f1.read()
# # print(m)
#
# f2= open('text2.txt')
# for line in f2:
#     print(line.lstrip() + "!")

# import smtplib
#
# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.starttls()
# smtpObj.login('n.sribna@gmail.com','dthjybrf2009')
# smtpObj.sendmail('n.sribna@gmail.com','n.sribna@gmail.com',"I did it!")
# smtpObj.quit()

import requests
# r = requests.get('https://pythonworld.ru/samouchitel-python')
# print(r.text)

resp = requests.get('https://ru.wikipedia.org/wiki/TCP/IP')
resp.status_code
print(resp.headers, sep = '\n')
print(resp.url)

url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

resp = r.json()
print (resp['headers'])

book = {'title':'Nata ber', 'author':'Nata'}

r = requests.post('http://pulse-rest-testing.herokuapp.com/books/', data = {'title': 'Price', 'author':'King'})
print(r.text, sep = "\n")
print (r.status_code)

base_url = 'http://pulse-rest-testing.herokuapp.com/books/'
book_id = r.json()
r = requests.delete(base_url + str(book_id["id"]))
print(r.text)
print(book_id)
print (r.status_code)
