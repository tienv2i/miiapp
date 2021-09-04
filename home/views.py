from django.shortcuts import render
from .forms import ContactMessageForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            status = 'form_saved'
        else:
            status = 'form_invalid'
    else:
        form = ContactMessageForm()
        status = 'form_nodata'

    return render(request, 'home/contact.html', { 'form': form, 'status': status, 'title': 'MiiApp - Contact me!' })