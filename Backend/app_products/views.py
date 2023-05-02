from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from app_products.models import Category, Product, Cart
from app_products.serialyzers import CategorySerializer, ProductSerializer, CartSerializer
from app_products.Paginators import CustomPagination, SalePagination



class CategoryView(APIView):
  def get(self, request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class ProductPopularView(APIView):
  def get(self, request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

class ProductDetailView(APIView):
  def get(self, request, pk):
    product = Product.objects.filter(pk=pk)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data[0])


class ProductLimitedView(APIView):
  def get(self, request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

class basket(APIView):

  def get(self, request):
    product = Cart.objects.all()
    serializer = CartSerializer(product, many=True)
    return Response(serializer.data)
  def post(self, request):
    try:
      product = Cart.objects.filter(product_id=request.data['id'])
      count = product[0].count
      count += int(request.data['count'])
      product.update(count=count)
    except:
      product = Cart.objects.create(product_id=request.data['id'],
                                    count=request.data['count'])
    serializer = CartSerializer(data=product)
    serializer.is_valid()
    return Response(serializer.data)

  def delete(self,request):
    try:
      product = Cart.objects.filter(product_id=request.query_params['id'])
      count = product[0].count
      count -= int(request.query_params['count'])
      product.update(count=count)
    except:
      product = Cart.objects.filter(product_id=request.query_params['id'])
      product.delete()
    serializer = CartSerializer(data=product)
    serializer.is_valid()
    return Response(serializer.data)



class ProductBannersView(APIView):
  def get(self, request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response({'banners':serializer.data})


class CatalogView(ListModelMixin, GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  pagination_class = CustomPagination

  def get(self, request):
    return self.list(request)


class ProductSalesView(ListModelMixin, GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  pagination_class = SalePagination

  def get(self, request):
    return self.list(request)


