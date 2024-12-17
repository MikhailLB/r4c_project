import json
from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .services import create_robot, get_weekly_data
from django.core.exceptions import ValidationError
from .utils import generate_excel

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


def export_robot_summary_data(request):

    """Экспортирует Excel-файл со сводкой производства за последнюю неделю."""

    weekly_summary = get_weekly_data()
    excel_file = generate_excel(weekly_summary)

    now = datetime.now()
    date = now.strftime('%Y_%m_%d')

    response = HttpResponse(
        excel_file,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = f'attachment; filename="weekly_production_summary_{date}.xlsx"'

    return response
