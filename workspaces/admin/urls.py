from django.urls import include, path
from rest_framework import routers
from workspaces.admin import views

router = routers.DefaultRouter()
#router.register(r'client_applications', views.ClientApplicationViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'schedules', views.ScheduleViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]