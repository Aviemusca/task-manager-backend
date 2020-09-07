from rest_framework.generics import CreateAPIView

from .models import Contact
from .serializers import ContactSerializer


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
