from django.http import FileResponse
from django.shortcuts import render
from django.views import View
from .models import Specification


class Landing(View):
    def get(self, request, *args, **kwargs):
        specification = Specification.objects.first()
        experiences = specification.experiences.all()
        educations = specification.educations.all()
        context = {'information': specification, 'experiences': experiences, 'educations': educations}
        return render(request, 'server/home.html', context, content_type='text/html', status=200)


class Resume(View):
    def get(self, request, *args, **kwargs):
        file = open(Specification.objects.first().cv.path, 'rb')
        return FileResponse(file, content_type='application/pdf', status=200)
