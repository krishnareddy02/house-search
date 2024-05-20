from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    # path('',views.home,name="home"),
    path('home_page',views.home_page,name="home_page"),
    path('registration',views.registration,name="registration"),
    path('book_details',views.book_details,name="book_details"),
    path('login_page',views.login_page,name="login_page"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('admin',views.admin,name="admin"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('seller_data',views.seller_data,name="seller_data"),
    path('books_data',views.books_data,name="books_data"),
    path('email/<int:id>',views.email,name='email')
]
