from rest_framework import status, generics, mixins
from rest_framework.response import Response

from .serializers import ContactSerializer
from .models import Contact


class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request):
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response('Message sent successfully!', status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

