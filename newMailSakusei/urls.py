"""
URL configuration for newMailSakusei project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from polls import views as polls_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # add index.html
    path('', polls_views.index, name='index'),
    path('reply/', polls_views.reply, name='reply'),
    path('privacy_policy/', polls_views.privacy_policy, name='privacy_policy'),
    path('customs_post/', polls_views.customs_post, name='customs_post'),

    # handle /api/generate post
    path('api/generate', polls_views.generate_email, name='generate_email'),
    path('api/add_emoji', polls_views.add_emoji, name='add_emoji'),
    path('api/more_polite', polls_views.more_polite, name='more_polite'),
    path('api/generateReply', polls_views.generate_reply, name='generate_reply'),
    path('api/translate', polls_views.translate_to_english, name='translate_to_english'),
    path('api/getHSCode', polls_views.fetch_hs_code, name='fetch_hs_code')

    # fix TypeError: view must be a callable or a list/tuple in the case of include()

]