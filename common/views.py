import requests

from rest_framework import viewsets, status
from rest_framework.views import APIView

def format_data(result):
    '''
    Method use for format response data in django generic and viewset apis
    '''
    if result.status_code in [200,201]:
        status = True
    else:
        status = False

    data = {
        'status':status,
        'status_code':result.status_code,
        'data':result.data
    }
    result.data = data

    return result


'''
This class is to manipulate response data of viewset
Developer needs to extend this class to use its functionalities
'''
class DataWrapperViewSet(viewsets.ModelViewSet):
    def dispatch(self, *args, **kwargs):
        result =  super(DataWrapperViewSet, self).dispatch(*args, **kwargs)
        data = format_data(result)
        return data


'''
This class is to manipulate response data for generic api views 
Developer needs to extend this class to use its functionalities
'''
class GenericAPIView(APIView):

    def dispatch(self, *args, **kwargs):
        result =  super(GenericAPIView, self).dispatch(*args, **kwargs)
        data = format_data(result)      
        return data

