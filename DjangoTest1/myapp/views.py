from django.http import HttpResponse

def index(request):
    return HttpResponse('''<html>
        <head><title>Index Page</title></head>
        <body>
            <h1>Welcome to the Index Page</h1>
            <a href="/data/">Go to Data Page</a><br>
            <a href="/test/">Go to Test Page</a>
        </body>
    </html>''')

def data(request):
    return HttpResponse('''<html>
        <head><title>Data Page</title></head>
        <body>
            <h1>This is the Data Page</h1>
            <a href="/">Back to Index</a><br>
            <a href="/test/">Go to Test Page</a>
        </body>
    </html>''')

def test(request):
    return HttpResponse('''<html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Welcome to the Test Page</h1>
            <a href="/">Back to Index</a><br>
            <a href="/data/">Go to Data Page</a>
        </body>
    </html>''')
