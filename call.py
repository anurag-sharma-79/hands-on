import plivo

auth_id = ""
auth_token = ""
p = plivo.RestAPI(auth_id, auth_token)

params = {
    'from': '+1111111111',
    'to': '+2222222222',
    'answer_url': 'https://gist.githubusercontent.com/anurag-sharma-79/27e801824a96633dc660ec587d171e90/raw/cc3bfebfb6310a9e3a44201d363fb68b11983847/IVR.xml',
    'answer_method': 'GET'
}
response = p.make_call(params)

print str(response)