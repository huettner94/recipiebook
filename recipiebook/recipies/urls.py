from django.urls import path
import recipies.views.recipie

urlpatterns = [
        path("", recipies.views.recipie.RecipieView.as_view()),
        path("<recipieid>/", recipies.views.recipie.RecipieView.as_view(),
             name="recipie"),
        ]
