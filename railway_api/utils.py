from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # if response is not None:
    #     response.data['status_code'] = response.status_code
    print(str(response))
    return make_generic_response(None,False,response.data.values())

def make_generic_response(data,isSuccess,message=''):
    resp_data = {'isSuccess': isSuccess,'message':message, 'data': data}
    return Response(resp_data)