from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import ClientCreateView, ClientListView, ClientDetailView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list_client'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('<int:pk>/client_detail/', ClientDetailView.as_view(), name='detail_client'),
]
