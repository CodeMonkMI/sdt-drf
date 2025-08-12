from django.db import router
from rest_framework import routers
from book.views import BookViewSet
from author.views import AuthorViewSet
from borrow_record.views import BorrowBookViewSet, ReturnBookViewSet

router = routers.SimpleRouter()

router.register(
    "books",
    BookViewSet,
)
router.register(
    "authors",
    AuthorViewSet,
)

router.register(
    "borrow",
    BorrowBookViewSet,
)
router.register("return", ReturnBookViewSet, basename="return")


urlpatterns = router.urls
