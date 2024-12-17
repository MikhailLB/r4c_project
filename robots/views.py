import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import create_robot
from django.core.exceptions import ValidationError

@csrf_exempt
def robot_processing(request):

    """ Представление обработки JSON """

    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            robot = create_robot(data)
            return JsonResponse({'status': 'success', 'robot_id': robot.id})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)

        except ValidationError as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid HTTP method'}, status=405)
