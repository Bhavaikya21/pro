from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('profile/',views.profile,name="profile"),
]
