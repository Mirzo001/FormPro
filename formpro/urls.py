from django.urls import path

from formpro.views import ContactListView
from .views import FormCreateView
urlpatterns = [
    path('',FormCreateView.as_view(), name='form_new'),
    path('xabarlar/', ContactListView.as_view(), name='contact_list'),
]