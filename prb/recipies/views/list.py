from django.views.generic import TemplateView
from recipies.models.recipie import Recipie

class ListView(TemplateView):
    template_name = "recipies/list.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['recipies'] = Recipie.objects.all()
        return context
