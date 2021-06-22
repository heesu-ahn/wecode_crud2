from django.urls import path
from curd2.views import OwnerView

urlpatterns = [
    path('',OwnerView.as_view())
]