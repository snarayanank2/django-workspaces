import logging

from rest_framework import viewsets
from workspaces.accounts.models import Account
from workspaces.accounts.serializers import AccountSerializer

logger = logging.getLogger(__name__)

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    ordering = 'created_at'