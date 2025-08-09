from email.mime import base
from os import path
from django.db import router
from django.urls import include
from rest_framework import routers
from book.views import BookViewSet
from author.views import AuthorViewSet
from borrow_record.views import BorrowBookViewSet, ReturnBookViewSet
from member.views import MemberViewSet

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
    "members",
    MemberViewSet,
)
router.register(
    "borrow",
    BorrowBookViewSet,
)
router.register("return", ReturnBookViewSet, basename="return")


urlpatterns = router.urls
