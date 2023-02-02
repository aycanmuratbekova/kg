from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializers import NewsSerializer

from .ru_date import get_ru_date


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = NewsSerializer(queryset, many=True)
    #
    #     for data in serializer.data:
    #         data['day_month'], data['year'] = get_ru_date(data['news_date'])
    #
    #     return Response({'count': len(queryset), 'results': serializer.data})
