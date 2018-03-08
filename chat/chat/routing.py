from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter


# websocket router
application = ProtocolTypeRouter({
    'websocket': URLRouter([

    ])
})
