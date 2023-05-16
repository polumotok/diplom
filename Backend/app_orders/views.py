from rest_framework.response import Response
from rest_framework.views import APIView
from app_orders.Serialyzers import OrderingGetSerializer, OrderingPostSerializer, PaymentSerializer
from app_orders.models import Orders, Order_product, Payment
from app_products.models import Cart


class OrderActiveView(APIView):
  def get(self, request):
    order = Orders.objects.all().first()
    serializer = OrderingGetSerializer(order)
    return Response(serializer.data)


class OrdersView(APIView):
  def get(self, request):
    order = Orders.objects.all().first()
    serializer = OrderingGetSerializer(order)
    return Response(serializer.data)

  def post(self, request):
    user = request.user.id
    product = request.data[0]['id']
    order = Orders.objects.get_or_create(profile_id=user)
    order_id = order[0]
    order_product = Order_product.objects.get_or_create(
      order_id=order_id.orderId,
      product_id=int(product),
      count=request.data[0]['count'],
      price=request.data[0]['price']
    )
    serializer = OrderingPostSerializer(data=order_product)
    serializer.is_valid()
    return Response(serializer.data)

class OrderRegisterView(APIView):
  def get(self, request, pk):
    info = Orders.objects.filter(orderId=pk)
    serializer = OrderingGetSerializer(info, many=True)
    print(request)
    return Response(serializer.data)
  def post(self, request, pk):
    info = Orders.objects.filter(orderId=pk)
    info.update(
      city=request.data['city'],
      address=request.data['address'],
      paymentType=request.data['paymentType'],
      deliveryType = True,
    )
    serializer = OrderingGetSerializer(info, many=True)
    return Response(serializer.data)

class PaymentView(APIView):
  def post(self, request):
    payment = Payment.objects.get_or_create(
      name=request.data['name'],
      month=request.data['month'],
      year=request.data['month'],
      code=request.data['code'],
    )
    product = Cart.objects.all()
    product.delete()
    serializer = PaymentSerializer(data=payment)
    serializer.is_valid()
    return Response(serializer.data)