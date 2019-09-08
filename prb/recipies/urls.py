from django.urls import path
import recipies.views.recipie
import recipies.views.list

urlpatterns = [
        path("", recipies.views.list.ListView.as_view()),
        path("recipie/<recipieid>/", recipies.views.recipie.RecipieView.as_view(), name="recipie"),
        ]
