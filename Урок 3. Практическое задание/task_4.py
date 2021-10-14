"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from hashlib import md5


class CacheUrl:
    def __init__(self):
        self.solt = "site_domain.com".encode()
        self.cache_info = {}

    def cache_url(self, url):
        if self.cache_info.get(url):
            print(f"{url} присутствует в кэше")
        else:
            url_hesh = md5(url.encode() + self.solt).hexdigest()
            self.cache_info[url] = url_hesh
            print(self.cache_info)


test = CacheUrl()
test.cache_url("https://www.google.com")
test.cache_url("https://www.google.com")