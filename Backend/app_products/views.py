from django.http import JsonResponse
from rest_framework.views import APIView
from app_products.models import Category,Product
from app_products.serialyzers import CategorySerializer


class CategoryView(APIView):
  def get(self, request):
    if request.method == 'GET':
      categories = Category.objects.all()
      serializer = CategorySerializer(categories, many=True)
      return JsonResponse(serializer.data, safe=False)

