from django.shortcuts import render
from django.template.context_processors import csrf
from imageapp.models import *
from imageapp.forms import FileFieldForm
from django.views.generic.edit import FormView

class UploadFileView(FormView):
    form_class = FileFieldForm
    template_name = 'upload_image.html'
    success_url = '.'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                imgfile = TImages(image=f)
                imgfile.save()
            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgdata'] = TImages.objects.all()
        return context
