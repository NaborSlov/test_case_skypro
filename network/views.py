from rest_framework import generics

from network import serializers
from network.models import Vendor


# class VendorRetrieve(generics.RetrieveAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = serializers.VendorSerializer
#
#
# class VendorCreate(generics.CreateAPIView):
#     model = Vendor
#     serializer_class = serializers.VendorCreateSerializer
