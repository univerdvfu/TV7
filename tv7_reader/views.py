from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from . import main
from .models import Sensor
import multiprocessing

def worker(device_id, data_type_list):
    try:
        sensor = Sensor.objects.get(tv_name=device_id)
        device = {
            'ip': sensor.ip,
            'port': sensor.port
        }
    except Sensor.DoesNotExist:
       device = {'error': 'Sensor not found'}
    print(device)
    results = main.run_sync_simple_client(comm="tcp", host=device['ip'], port=device['port'], registers_name_kist=data_type_list)
    print(results)
    return results
@csrf_exempt
def json_read(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        names = data.get('name', [])
        data_sensor = data.get('data', [])
        results = multiprocessing.Manager().list()
        print (names)
        # response_data = main.run_sync_simple_client(comm="tcp", host="10.61.32.50", port="502", registers_name_kist=data_sensor)
        # # print(main.run_sync_simple_client(registers_name_kist=request_data_list))
        for name in names:
            response_data = multiprocessing.Process(target=worker, args=(name, data_sensor))
        print(response_data)
        # print(response_data.keys())
        return JsonResponse(data, status=405)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)