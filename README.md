# api_final
Этот проект служит сервером для django_spring4, только django_spring4 не являестся SPA, как было показано в примере, поэтому их соединение работать не будет, однако идея общая

### Как запустить проект:
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
. venv/Script/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

