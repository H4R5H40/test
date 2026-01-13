from django.conf import settings
from supabase import create_client

# initialize once
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

# def add(expense_data):
#     a=(((supabase.table("expenses").select('*').execute()).data)[0])['amount']
#     return a
def add(expense_data):
    response = supabase.table("expenses").insert(expense_data).execute()
    return response.data

