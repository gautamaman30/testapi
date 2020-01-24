from django.urls import path
from .views import ApiRoot, SearchByAll, SearchByBranch


urlpatterns = [
    path('', ApiRoot.as_view()),
    path('api/branches/autocomplete/', SearchByBranch.as_view()),
    path('api/branches/', SearchByAll.as_view()),
]
