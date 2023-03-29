from.views import *
from django.urls import path


urlpatterns = [
    path("",VcardList.as_view())
]
