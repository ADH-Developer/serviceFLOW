from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/customers/appointments/$", consumers.AppointmentConsumer.as_asgi()),
    re_path(r"ws/admin/workflow/$", consumers.WorkflowConsumer.as_asgi()),
]