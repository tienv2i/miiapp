from django.shortcuts import render
from .forms import DocumentForm

# Create your views here.
def index(request):
    if request.method=='POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            status = 'file_saved'
        else:
            status = 'file_invalid'
    else:
        form = DocumentForm()
        status = 'file_selectting'
    return render(request, 'uploader/index.html', {
        'form': form,
        'status': status,
        'title': 'MiiApp - Uploader'
    })