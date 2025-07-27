#from django.shortcuts import render,HttpResponse

# Create your views here.
# replicate_app/views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .replicator import replicate_file

@csrf_exempt
def replicate_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        data = json.loads(request.body)
        s3_bucket = data.get('s3_bucket')
        s3_key = data.get('s3_key')

        if not s3_bucket or not s3_key:
            return JsonResponse({'error': 'Missing s3_bucket or s3_key'}, status=400)

        result = replicate_file(s3_bucket, s3_key)
        return JsonResponse({'status': result}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

