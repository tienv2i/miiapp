from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import DocumentForm
from .models import Document

# Create your views here.
@staff_member_required
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
    docs = Document.objects.order_by('-uploaded_at').all()
    page_number = request.GET.get('page')
    paginator = Paginator(docs, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'uploader/index.html', {
        'form': form,
        'status': status,
        'title': 'MiiApp - Uploader',
        'docs': docs,
        'paginator': paginator,
        'page_obj': page_obj
    })

# class DocumentListView(ListView):
#     model = Document
#     paginate_by = 2
#     template_name = 'uploader/files'