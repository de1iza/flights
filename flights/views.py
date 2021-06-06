from django.http import JsonResponse
from django.http import Http404
from flights.models import Flight


def flight_info(request, flight_id):
    """
    Displays /flight/<id> and shows flight info in JSON

    :param request: WSGIRequest object
    :param flight_id: integer
    :return: JSON
    """
    try:
        data = Flight.objects.get(pk=flight_id).get_info()
    except Flight.DoesNotExist:
        raise Http404('Flight does not exist')
    return JsonResponse(data)
