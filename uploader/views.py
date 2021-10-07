from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AttachmentForm
from .models import Attachment

# Create your views here.
@login_required(login_url='/admin/login/')
def index(request):
    if request.method=='POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            status = 'file_saved'
        else:
            status = 'file_invalid'
    else:
        form = AttachmentForm()
        status = 'file_selectting'
    docs = Attachment.objects.order_by('-uploaded').all()
    page_number = request.GET.get('page')
    paginator = Paginator(docs, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'uploader/index.html', {
        'form': form,
        'status': status,
        'title': 'MiiApp - Uploader',
        'page_obj': page_obj
    })

# class AttachmentListView(ListView):
#     model = Attachment
#     paginate_by = 2
#     template_name = 'uploader/files'