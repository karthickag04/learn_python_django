from django.urls import path


from . import views

urlpatterns = [
    path('', views.lib_index, name='lib_index'),
    path('catalog/', views.catalog, name='catalog'),
    path('membership/', views.membership, name='membership'),
    path('book_borrowing/', views.book_borrowing, name='book_borrowing'),
    path('library_events/', views.library_events, name='library_events'),
    path('contact_us/', views.contact_us, name='contact_us'),
]