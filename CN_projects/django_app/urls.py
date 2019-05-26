from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    path('project/<str:proj_id>/assign-mentor/<str:user_id>/', assign_mentor),
    path('users/<str:user_id>/projects/', get_projects),
    path('users/<str:user_id>/mentees/', get_mentees),
    path('project/<str:proj_id>/get-user-mentor/', get_user_mentor),
    path('users/<str:user_id>/assign-project/<str:proj_id>/', assign_project),
    path('users/', create_user),
    path('project/', create_project),
]