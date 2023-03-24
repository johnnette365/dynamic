from django.shortcuts import render


def handler_404(request, exception):
    # return render(request, '404.html', status=404)
    return render(request, '404.html', status=404)