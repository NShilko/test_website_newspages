from django.shortcuts import render


def page_not_found_view(request, exception):
    print('not found')
    return render(request, '404.html')
