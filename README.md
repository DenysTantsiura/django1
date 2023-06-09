# django1

Learning django

# -------------------------------

poetry add django

python -m django --version

створення проекту mysite
django-admin startproject mysite

запустити локально сервер для розробки
знаходячись всередині папки проекту mysite (cd mysite)
python manage.py runserver

Кожен проект може складатися з кількох застосунків. Застосунки також можуть бути одночасно частиною кількох проектів.
можемо створити перший застосунок polls
python manage.py startapp polls

додамо код у файл polls/views.py

Далі, щоб представлення стало видимим, його потрібно зареєструвати.
Для цього створимо модуль polls/urls.py

Щоб зареєструвати сам застосунок polls, у проекті потрібно модифікувати mysite/urls.py

Щоб переглянути результат роботи нашого застосунку, можна виконати python manage.py runserver та перейти на http://localhost:8000/polls/.
poetry add django

python -m django --version

створення проекту mysite
django-admin startproject mysite

запустити локально сервер для розробки
знаходячись всередині папки проекту mysite (cd mysite)
python manage.py runserver

Кожен проект може складатися з кількох застосунків. Застосунки також можуть бути одночасно частиною кількох проектів.
можемо створити перший застосунок polls
python manage.py startapp polls

додамо код у файл polls/views.py

Далі, щоб представлення стало видимим, його потрібно зареєструвати.
Для цього створимо модуль polls/urls.py

Щоб зареєструвати сам застосунок polls, у проекті потрібно модифікувати mysite/urls.py

Щоб переглянути результат роботи нашого застосунку, можна виконати python manage.py runserver та перейти на http://localhost:8000/polls/.

# --------------------------------------

(Щоб синхронізувати стан моделей у Python та таблиць у базі даних достатньо виконати команду python manage.py migrate. Команда migrate "дивиться" в INSTALLED_APPS в mysite/settings.py і створює всі необхідні таблиці в базі даних для всіх застосунків.
створимо моделі для нашого застосунку polls. Для цього перепишемо модуль polls/models.py

Тепер потрібно зареєструвати застосунок у проекті, щоб інструмент міграцій знав про ці моделі. Для цього потрібно додати наш застосунок polls до списку застосунків, константа INSTALLED_APPS у файлі mysite/settings.py

Для створення міграції для нашого застосунку: python manage.py makemigrations polls.
( Міграції ще не застосовувалися, ви можете подивитися, що повинно бути зроблено в міграціях, та змінити цей файл, якщо потрібно.

Щоб застосувати всі міграції: python manage.py migrate.
(Щоб змінити налаштування роботи з базою даних, потрібно змінити значення константи DATABASES у файлі mysite/settings.py. Django налаштований на роботу з SQLite за замовчуванням.

# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

Щоб показати, як використовувати моделі у представленні, змінимо файл polls/views.py

(Але самі дані в базі даних поки що відсутні, і щоб їх додати туди, потрібна адмін-панель.

python manage.py migrate
потрібно спочатку створити користувача, який зможе зайти в адмін панель:
python manage.py createsuperuser

Після того, як користувач успішно створений, ви можете запустити сервер і зайти на http://127.0.0.1:8000/admin/, використовуючи ім'я та пароль для нового користувача.
python manage.py runserver
зайти на http://127.0.0.1:8000/admin/

зареєструємо таблиці Question та Choice в адмін-панелі. Для цього у файлі polls/admin.py додамо наступні рядки:
admin.site.register(Question)
admin.site.register(Choice)

Тепер ви можете додавати питання для застосунку polls, використовуючи адмін-панель.

Аргументи запиту
Давайте додамо ще представлень у файл polls/views.py
І зареєструємо ці представлення у файлі polls/urls.py:

Щоб Django автоматично виявив шаблони застосунку, потрібно в пакеті застосунку створити папку polls/templates/polls. Усі HTML документи у цій папці будуть сприйняті як шаблони.

І оновимо файл polls/views.py таким чином, щоб використати цей шаблон

Обробка форм
Давайте створимо просту форму для вибору відповіді на запитання. Для цього створимо шаблон форми в polls/templates/polls/detail.html

Додамо тепер обробник форм у polls/urls.py
path('<int:question_id>/vote/', views.vote, name='vote'),

І створимо функцію обробник vote у polls/views.py

Додамо обробник результатів у polls/views.py
def results

І відповідний йому шаблон у polls/templates/polls/results.html

Також потрібно оновити представлення pools/views.py функцію detail

# ------------------------------------------

python manage.py runserver
