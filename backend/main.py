
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import supabase, add
def index(request):
    try:
        from supabase import create_client, Client
        return JsonResponse({"status": "backend lol reached"})
    except Exception as e:
        return JsonResponse({"status": e})
@csrf_exempt
def addData(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    try:
        body = json.loads(request.body.decode("utf-8"))

        # Extract split users
        split_users = body.pop("split_users", [])
        if not split_users:
            return JsonResponse({"error": "No users selected"}, status=400)

        # Insert main expense
        response = add(body)
        expense_id = response.data[0]["id"]

        # Insert splits
        share = body["amount"] / len(split_users)
        split_rows = [
            {"expense_id": expense_id, "user_id": uid, "share_amount": round(share, 2)}
            for uid in split_users
        ]
        supabase.table("expense_splits").insert(split_rows).execute()

        return JsonResponse({"status": "success", "expense_id": expense_id})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        print("ERROR:", e)  # check PythonAnywhere error log
        return JsonResponse({"error": "Server error"}, status=500)
@csrf_exempt
def addData(request):
    test_expense = {
    "title": "Test Expense",
    "amount": 1000,
    "paid_by": "harsh",
    "category": "travel",
    "expense_date": "2026-01-12",
    "description": "Dry run insert from Django"
    }
    try:
        response = add(test_expense)
        return JsonResponse({
            "status": "success",
            "message": "Data inserted"
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

