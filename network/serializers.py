from rest_framework import serializers

from .models import Contact, Product, Factory, RetailsNet, IndiPred


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Factory
        fields = "__all__"


class RetailSerializer(FactorySerializer):
    class Meta:
        model = RetailsNet
        fields = "__all__"


class IndividualSerializer(RetailSerializer):
    class Meta:
        model = IndiPred
        fields = "__all__"
