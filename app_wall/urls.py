from django.urls import path
from . import views

urlpatterns =[
    path('', views.wall_index),
    path('logout', views.logout),
    path('message', views.post_message),
    path('<int:message_id>/comment', views.post_comment),
    path('<int:message_id>/edit', views.edit_message),
    path('<int:comment_id>/delete', views.delete_comment)
]