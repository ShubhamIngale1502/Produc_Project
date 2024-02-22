from rest_framework.decorators import api_view
from .serializer import UserSerializer
import logging
from rest_framework.response import Response

logger = logging.getLogger('mylogger')

@api_view(http_method_names=('GET','POST'))
def user_api(request):
    if request.method == 'POST':
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
           
            logger.info('User Created SuccesFully')
            return Response(data=serializer.data, status=201)
        except:
            logger.error('User Creating Product')
            return Response(data=serializer.errors, status=404)
    
    


