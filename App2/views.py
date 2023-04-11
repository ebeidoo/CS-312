from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    html='''
      <!DOCTYPE html>
        <html>
        <body>

        <p>This is a paragraph.</p>
        <p>This is a paragraph.</p>

        </body>
        </html>
    '''
    return HttpResponse(html)

