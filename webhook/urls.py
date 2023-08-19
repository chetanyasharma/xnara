from django.urls import path

from .views import Webhook

urlpatterns = [
    path('packed_data', Webhook.as_view()),
]
