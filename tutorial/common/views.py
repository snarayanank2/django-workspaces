import logging

from django.contrib.auth.models import User
from django.db.models import Exists, OuterRef
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import (authentication, filters, permissions, status,
                            viewsets)
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from saas_framework.attachments.models import Attachment
from saas_framework.attachments.views import AttachmentViewSet
from saas_framework.comments.views import CommentViewSet
from saas_framework.tags.views import TagViewSet
from saas_framework.tpas.views import (ThirdPartyAppInstallViewSet,
                                       ThirdPartyAppViewSet)
from saas_framework.workspaces.models import Workspace
from saas_framework.workspaces.views import WorkspaceViewSet
from saas_framework.sharing.mixins import SharingModelViewSetMixin

logger = logging.getLogger(__name__)

class AttachmentViewSet(SharingModelViewSetMixin, AttachmentViewSet):
    pass

class TagViewSet(SharingModelViewSetMixin, TagViewSet):
    pass

class CommentViewSet(SharingModelViewSetMixin, CommentViewSet):
    pass
