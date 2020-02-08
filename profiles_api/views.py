from rest_framework.views import APIView
from rest_framework.response import Response

class Hello_APIView(APIView):
    """ Create a API """
    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP method as function to (get,post.patch,put,delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to urls',
        ]

        return Response({'message':"Hello!",'an_apiview':an_apiview})
