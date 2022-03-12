from django.urls import path
from apps.uapi import views


urlpatterns = [
    path('create-session/', views.start_new_test_session),
    path('topic-ids/', views.get_topic_ids),
]