from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """
    View for the home page.
    """
    
    context = {
        'documents': [
            {'id': 1, 'title': 'Passport', 'icon': 'fa-file-image'},
            {'id': 2, 'title': 'Client Profile', 'icon': 'fa-file-word'},
            {'id': 3, 'title': 'Account Opening Form', 'icon': 'fa-file-pdf'},
            {'id': 4, 'title': 'Client Description', 'icon': 'fa-file-text'},
        ],
        'document_status': None
    }
    return render(request, 'home.html', context)

def document_view(request, doc_id):
    """
    View for displaying a specific document.
    """
    # Here you would get the document data from wherever it's stored
    doc_data = {
        'title': f'Document {doc_id}',
        'content': f'Content of document {doc_id}',
        'date': '2023-01-01',
        'author': 'Author',
    }
    
    context = {
        'document_id': doc_id,
        'document_data': doc_data,
    }
    
    return render(request, f'viewer/document_{doc_id}.html', context)
