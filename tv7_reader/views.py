from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from . import main
@csrf_exempt
def json_read(request):
    if request.method == 'POST':
        request_data_list = json.loads(request.body)
        print(request_data_list)


        response_data = main.run_sync_simple_client(comm="tcp", host="10.61.32.50", port="502", registers_name_kist=request_data_list)
        # print(main.run_sync_simple_client(registers_name_kist=request_data_list))
        print(response_data)
        # print(response_data.keys())
        
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)