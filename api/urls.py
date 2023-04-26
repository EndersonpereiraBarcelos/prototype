from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliarioViewSet, LavaJatoViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'fundos', FundoImobiliarioViewSet)

urlpatterns = router.urls


app_name = 'lavajato'

router = DefaultRouter(trailing_slash=False)
router.register(r'lavajato', LavaJatoViewSet)

urlpatterns = router.urls