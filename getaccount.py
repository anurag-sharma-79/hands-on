import plivo

auth_id = ""
auth_token = ""
p = plivo.RestAPI(auth_id, auth_token)


response = p.get_account()

print str(response)