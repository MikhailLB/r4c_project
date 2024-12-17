import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from orders.services import create_order


@csrf_exempt
def create_order_processing(request):

    """ Представление обработки заказа JSON """
    if request.method == 'POST':
        try:
             data = json.loads(request.body)

             order = create_order(data)
             return JsonResponse({'status': 'success', 'order_id': order.id})

        except json.JSONDecodeError:
             return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)

        except ValidationError as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

        except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid HTTP method'}, status=405)
