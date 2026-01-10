from supabase import create_client, Client
url='https://nzviaqzmtjxaftppfyrn.supabase.co'
key='sb_publishable_yGieFlaaPLEQPZrh-_OJYA_ddjnFiey'
# sb_secret_Lp-pqG8i7_dVhlbOy-a9OQ_q5ZV3iIv
supabase: Client = create_client(url, key)
connection = supabase.schema("public")
def auth(email,password):
    data = (connection.schema("public").table("id_pass").select("*").eq("id", email).eq("password", password).execute()).data
    print("DATA:",data)
    return data[0]