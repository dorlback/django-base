from django.urls import path
from book_app.views import BookListView

urlpatterns = [
    path("/list", BookListView.as_view(), name="book-list"),
]