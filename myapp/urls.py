from django.urls import path
from .views import contact, snippet_detail

urlpatterns = [
    path('', contact, name='contact'),
    path('snippet', snippet_detail, name='snippet_detail')
]