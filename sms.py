import plivo


auth_id = ""
auth_token = ""
p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': 'plivo', 
    'dst' : '+111111111111', 
    'text' : u"Hello, how are you?"
}
response = p.send_message(params)

print str(response)