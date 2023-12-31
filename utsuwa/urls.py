from django.urls import path, include
from .views import *

app_name = 'utsuwa'

urlpatterns = [
    path('', home, name='home'),
    path('access', access, name='access'),
    path('contact', contact, name='contact'),
    path('services', services, name='cervices'),
    path('news', news, name='news'),
    path('qanda', questions, name='help'),
    path('business', service_business, name='business'),
    path('creative', service_creative, name='creative'),
    path('technology', service_tech, name='technology'),
    path('finances', service_finance, name='finances'),
]