from django.urls import path
from . import views

urlpatterns=[
    path('add-expense/',views.add_expense,name='add_expense'),
    path('view-expenses/',views.view_expenses,name='view_expenses'),
]
