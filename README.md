Articles
============

Виртуальное окружение
------------
В корневой директории **articles** необходимо создать файл **.env** с переменными виртуального окружения:  
    
    # articles/.env
    
    SECRET_KEY=KEY
    DEBUG=True
    ALLOWED_HOSTS=.127.0.0.1, .localhost

    DB_NAME=name
    DB_USER=django
    DB_PASSWORD=password

Эндпоинты:
------------
1. Регистрация :: POST :: https://tests-alex-maksimeniuk.ru/api/v1/auth/signup/
2. Создание статьи :: POST :: https://tests-alex-maksimeniuk.ru/api/v1/article/create/
3. Изменение статьи :: PUT :: https://tests-alex-maksimeniuk.ru/api/v1/article/1/update/
4. Удаление статьи :: DELETE :: https://tests-alex-maksimeniuk.ru/api/v1/article/1/destroy/
5. Список публичных статей :: GET :: https://tests-alex-maksimeniuk.ru/api/v1/article/list/
6. Публичная статья :: GET :: https://tests-alex-maksimeniuk.ru/api/v1/article/1/
7. Список закрытых статей :: GET :: https://tests-alex-maksimeniuk.ru/api/v1/subscription/list/
8. Закрытая статья :: GET :: https://tests-alex-maksimeniuk.ru/api/v1/subscription/2/

Регистрация
------------

    {
      'email': 'foo@example.ru',
      'password': 'password',
      'role': 1   # Необязательный параметр (default=2), где 1 - Автор, 2 - Подписчик
    }
    
Создание статей
------------

    {
      'title': 'Foo',
      'content': 'Foo Bar',
      'is_private': True   # Необязательный параметр (default=False)
    }
