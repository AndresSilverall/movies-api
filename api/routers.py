from rest_framework import routers
from . import viewsets


router = routers.DefaultRouter()

router.register(r"products/", viewsets.test_viewset)
urlpatterns = router.urls