from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from app_products.models import Category, Product, Cart, tags, Review
from app_products.serialyzers import (
    CategorySerializer,
    ProductSerializer,
    CartSerializer,
    ReviewSerializer,
)
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
            product = Cart.objects.filter(product_id=request.data["id"])
            count = product[0].count
            count += int(request.data["count"])
            product.update(count=count)
        except:
            product = Cart.objects.create(
                product_id=request.data["id"], count=request.data["count"]
            )
        serializer = CartSerializer(data=product)
        serializer.is_valid()
        return Response(serializer.data)

    def delete(self, request):
        try:
            product = Cart.objects.filter(product_id=request.query_params["id"])
            count = product[0].count
            count -= int(request.query_params["count"])
            product.update(count=count)
        except KeyError:
            product = Cart.objects.filter(product_id=request.query_params["id"])
            product.delete()
        serializer = CartSerializer(data=product)
        serializer.is_valid()
        return Response(serializer.data)


class ProductBannersView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response({"banners": serializer.data})


class CatalogView(ListModelMixin, GenericAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = Product.objects.filter(
            category=self.request.META["HTTP_REFERER"].split("/")[4]
        )

        title = self.request.query_params["filter[name]"]
        min_price = self.request.query_params["filter[minPrice]"]
        max_price = self.request.query_params["filter[maxPrice]"]
        ordering = self.request.query_params["sort"]

        if ordering:
            queryset = queryset.order_by(ordering)

        if title is not "":
            queryset = queryset.filter(title=title)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        return self.list(request)


class ProductSalesView(ListModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = SalePagination

    def get(self, request):
        return self.list(request)


class ReviewView(APIView):
    def get(self, request, pk):
        review = Review.objects.filter(product_id=pk)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        review = Review.objects.create(
            product_id=pk,
            author=request.data["author"],
            email=request.data["email"],
            text=request.data["text"],
            rate=request.data["rate"],
        )
        serializer = ReviewSerializer(data=review)
        serializer.is_valid()
        return Response(serializer.data)
