from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliarioViewSet, LavaJatoViewdSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'fundos', FundoImobiliarioViewSet)

urlpatterns = router.urls



app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'lavajato',LavaJatoViewdSet)
urlpatterns = router.urls
