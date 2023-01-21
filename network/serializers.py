from rest_framework import serializers

from .models import Vendor, Contact, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    product = ProductSerializer()

    class Meta:
        model = Vendor
        fields = "__all__"


class VendorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ("title", "type", "vendor")

    def save(self, **kwargs):
        if self.validated_data["type"] != 0:
            hierarchy = self.validated_data["vendor"].hierarchy + 1
            kwargs["hierarchy"] = hierarchy
        super().save(**kwargs)
