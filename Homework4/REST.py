# Тестовое приложение с REST API  http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
# •	Создаёт персонажа POST /roles/, вы запоминаете его id.
# •	Проверяете, что он создался и доступен по ссылке GET /roles/[id]
# •	Проверяете, что он есть в списке пользователей по GET /roles/
# •	Изменяете этого пользователя методом PUT roles/[id]/
# •	Проверяете, что он изменился и доступен по ссылке /roles/[id]
# •	Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
# •	Удаляете этого пользователя методом DELETE roles/[id]
# Второй скрипт: тоже самое с книгами  http://pulse-rest-testing.herokuapp.com/roles/

import requests

url = "http://pulse-rest-testing.herokuapp.com/roles/"
data = {'name':'NataB', 'type':'student2'}
r = requests.post(url, data )
book_id = r.json()
id = book_id['id']

rr = requests.get(url + str(id))
print(rr.text)

rr = requests.put(url + str(book_id['id']) +'/', data = {'name':'NatalyB', 'type':'student3'})
print(rr.text)

rr = requests.delete(url + str(book_id['id']) +'/')
print(rr.text)