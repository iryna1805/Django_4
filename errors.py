from django.http import HttpResponseNotAllowed, HttpResponseServerError, HttpResponseNotFound


def handle_404(request, exception):
    return HttpResponseNotFound('<h1>404 - Сторінку не знайдено</h1>')

def handle_500(request):
    return HttpResponseServerError('<h1>500 - Внутрішня помилка сервера</h1>')

def method_not_allowed(request, exception=None):
    return HttpResponseNotAllowed(['GET'], '<h1>405 - Метод не дозволено</h1>')
