from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lighthouse, Lighthouse_Result
from .serializers import LighthouseResultSerializer, LighthouseSerializer
from .pagination import PageNumberWithPageSizePagination

class LighthouseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = PageNumberWithPageSizePagination
    serializer_class = LighthouseSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['url', 'last_updated']

    filterset_fields = ['url', 'scheduled']

    def get_queryset(self):
        return Lighthouse.objects.for_user(self.request.user).order_by('-last_updated')


class LighthouseResultViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = PageNumberWithPageSizePagination
    serializer_class = LighthouseResultSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['url', 'timestamp']
    filterset_fields = ['url']

    def get_queryset(self):
        return Lighthouse_Result.objects.for_user(self.request.user).order_by('-timestamp')
