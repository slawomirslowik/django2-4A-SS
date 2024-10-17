from django.urls import path
from . import views
from mysite import views2

urlpatterns = [
    path("", views.index, name="index"),
        # ex: /polls/5/
    path("<int:question_id>/", views2.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]