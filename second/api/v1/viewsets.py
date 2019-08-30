from rest_framework.viewsets import ModelViewSet
from second.models import SecondHello
from .serializers import SecondHelloSerializer


class SecondHelloViewSet(ModelViewSet):
    serializer_class = SecondHelloSerializer
    queryset = SecondHello.objects.all()
