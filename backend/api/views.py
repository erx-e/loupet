import json
from django.http import JsonResponse

def api_home(request, *arg, **kwargs):

    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data.keys())
    data['params'] = dict(request.GET) # url query params
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)