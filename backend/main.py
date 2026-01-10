from .db import auth
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    try:
        data = json.loads(request.body.decode())
        print(data['id']+'  '+data['password'])
        print(auth(data['id'],data['password']))
    except Exception as e:
        print("JSON ERROR:", e)
        return JsonResponse({"error": "Bad JSON"}, status=400)

    return JsonResponse({"status": "backend reached"})
