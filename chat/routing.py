from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url('<str:room_name>/', consumers.ChatConsumer),
]