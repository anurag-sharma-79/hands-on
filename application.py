import plivo

auth_id = ""
auth_token = ""
p = plivo.RestAPI(auth_id, auth_token)

params = {
    'app_id': '24508368856390822'
}
response = p.get_application(params)

print str(response)