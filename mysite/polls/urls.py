# щоб представлення стало видимим, його потрібно зареєструвати. Для цього створимо модуль polls/urls.py
from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [  # в якому будуть маршрути для нашого застосунку.
    # один маршрут під час звернення до застосунку polls і він оброблятиметься функцією index з файлу views.py. 
    # Цьому маршруту даємо ім'я index. Тепер кореневий каталог програми polls буде дозволений за допомогою views.index
    # ex: /polls/
    path('', views.index, name='index'), 
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # Додамо тепер обробник форм
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''
Зверніть увагу на аргументи запиту, визначені у форматі <int:question_id>/. 
Тепер шлях /polls/34/ буде оброблений представленням views.detail, куди 
як аргумент question_id буде передано число 34. 
Також ми додали ім'я застосунку app_name = 'polls'. Це необхідно, щоб 
працювали конструкції виду <a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>
'''
