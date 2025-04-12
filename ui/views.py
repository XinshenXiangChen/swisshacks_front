from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import json
import os

def get_documents_data():
    """
    Get all documents data from the single JSON file.
    """
    json_file = os.path.join(settings.BASE_DIR, 'data', 'documents.json')
    
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def home(request):
    """
    View for the home page.
    """
    documents = [
        {'id': 1, 'title': 'Passport', 'icon': 'fa-passport'},
        {'id': 2, 'title': 'Client Profile', 'icon': 'fa-user'},
        {'id': 3, 'title': 'Account', 'icon': 'fa-university'},
        {'id': 4, 'title': 'Client', 'icon': 'fa-address-card'}
    ]
    
    # Get document status from the JSON
    docs_data = get_documents_data()
    if docs_data and 'inconsistencies' in docs_data:
        doc_status = docs_data['inconsistencies']
    else:
        doc_status = {
            'all_valid': True,
            'messages': [],
            'length': 4
        }
    
    return render(request, 'home.html', {
        'documents': documents,
        'document_status': doc_status
    })

def document(request, doc_id):
    docs_data = get_documents_data()
    if not docs_data:
        return render(request, f'viewer/document_{doc_id}.html', {
            'document_data': None,
        })

    # Map document IDs to their corresponding sections in the JSON
    doc_map = {
        2: 'client_profile',
        3: 'account',
        4: 'client'
    }

    if doc_id == 1:
        # For passport document, use the passport view
        return passport(request)
    elif doc_id == 3:
        # For document 3, pass the entire documents data
        return render(request, f'viewer/document_{doc_id}.html', {
            'document_data': docs_data
        })
    elif doc_id in doc_map:
        section = doc_map[doc_id]
        if section in docs_data:
            return render(request, f'viewer/document_{doc_id}.html', {
                'document_data': docs_data[section]
            })
    
    return render(request, f'viewer/document_{doc_id}.html', {
        'document_data': None
    })

def passport(request):
    # Get document data from JSON
    docs_data = get_documents_data()
    
    if docs_data and 'passports' in docs_data:
        # Get passport data and validation status directly from the JSON
        passport_data = docs_data['passports']['fields']
        field_status = docs_data['passports']['validation']
    else:
        # If no data is found or no passport section, return empty values
        passport_data = {}
        field_status = {}
    
    return render(request, 'viewer/document_1.html', {
        'passport_data': passport_data,
        'field_status': field_status,
    })
