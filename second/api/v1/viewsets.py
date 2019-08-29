from rest_framework import viewsets

from second.models import SecondHello


class SecondHelloViewSet(viewsets.ModelViewSet):
    queryset = SecondHello.objects.all()