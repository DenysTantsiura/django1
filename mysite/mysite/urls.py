"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


'''
    # шлях до створеного застосунку: polls/. Функція include потрібна, щоб повідомити Django, що всі маршрути, 
    # що починаються з polls/, повинні оброблятися застосунком polls. 
    # (Сам маршрут втрачає префікс polls (відбудеться заміна polls/ на /) і відправляється для обробки 
    # вже в сам застосунок.)
    path('polls/', include('polls.urls')),

    # шлях до адмін-панелі нашого проекту — admin/
    path('admin/', admin.site.urls),
'''