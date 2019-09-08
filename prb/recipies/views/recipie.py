from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from recipies.models.recipie import Recipie


class RecipieView(TemplateView):
    template_name = "recipies/recipie.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['recipies'] = Recipie.objects.all()
        if "recipieid" in kwargs:
            context['recipie'] = get_object_or_404(Recipie,
                                                   pk=kwargs['recipieid'])
        return context
