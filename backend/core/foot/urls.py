from django.urls import path
from .views import FootDetailView, FootListView

app_name = "foot"
urlpatterns = [
    path('foots/', FootListView.as_view(), name="foot-list"),
    path('foot/<foot_id>/', FootDetailView.as_view(), name="foot-detail"),
]
