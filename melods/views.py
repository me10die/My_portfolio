from django.views.generic import TemplateView

class Home(TemplateView):
    template_name='pages/home.html'

class About(TemplateView):
    template_name='pages/about.html'

class Skills(TemplateView):
    template_name='pages/skills.html'

class Contact(TemplateView):
    template_name='pages/contact.html'

class Cv(TemplateView):
    template_name='pages/cv.html'