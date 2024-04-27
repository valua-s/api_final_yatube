# api_final
Данный проект создан как платформа для создания постов о своей жизни интересах и просто о том что нравится.
Социальная сеть, где вы можете создавать посты, комментировать записи, а также делиться интересными картинками и подписываться на других пользователей.
Для того чтобы просматривать посты, ничего не понадобится, 
  но для полноценного взаимодействия со всеми возможностями приложения Вам понадобится зарегистрироваться на платформе.
api final
**Для запуска на своем компьютере на Windows**
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

**Некоторые примеры GET-запрососв, к кототорым Вы сможете обратиться без дополнительной регистриции, лишь запустив проект на своем компьютере**
```
http://127.0.0.1:8000/api/v1/posts/
```
Для получения списка всех доступных постов пользователей
```
http://127.0.0.1:8000/api/v1/posts/{номер_поста}/
```
Для получения отдельного поста
