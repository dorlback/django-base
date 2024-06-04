from django.urls import path
from book_app.views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path("list", BookListCreateView.as_view(), name="book-list-create"),
    path('list/<int:pk>', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-destroy'),
]

