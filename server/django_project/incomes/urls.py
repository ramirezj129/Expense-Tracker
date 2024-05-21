# urls.py

from django.urls import path
from .views import add_income, income_list

urlpatterns = [
    path('add-income/', add_income, name='add_income'),
    path('income-info/', income_list, name='income_list'),
    # Add other URL patterns as needed
]
