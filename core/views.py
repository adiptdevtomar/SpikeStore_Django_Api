from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'First',
            'Second',
            'Third',
            'Fourth'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message woth our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'methos': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'delete'})
