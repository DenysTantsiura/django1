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
#-------------------------
