from rest_framework.viewsets import ModelViewSet
from .models import (
    Gisement,
    Site
)
from .serializers import (
    GisementSerializer,
    SiteSerializer
)


class GisementViewSet(ModelViewSet):
    model = Gisement
    serializer_class = GisementSerializer
    queryset = Gisement.objects.all()

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related('site')
        return qs


class SiteViewSet(ModelViewSet):
    model = Site
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
