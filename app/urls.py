from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from ussd.views import AfricasTalkingUssdGateway
from . import views

from health_check.views import health_check

urlpatterns = [
    path("", views.index, name="home"),
    path('admin/', admin.site.urls),
    path('health/', health_check),
    url(r'^zynance',
        AfricasTalkingUssdGateway.as_view(),
        name='zynance-url')
    ]