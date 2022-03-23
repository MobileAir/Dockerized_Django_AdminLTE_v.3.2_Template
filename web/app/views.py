from django.shortcuts import render


def custom_handler404(request, exception):
    context = {}
    response = render(request, 'app/error_404.html', context=context)
    response.status_code = 404
    return response


def custom_handler500(request):
    context = {}
    response = render(request, 'app/error_500.html', context=context)
    response.status_code = 500
    return response


def index(request):
    return render(request, 'app/index.html', {})


def about(request):
    return render(request, 'app/about.html', {})
