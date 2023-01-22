from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Contact, Product, Factory, RetailsNet, IndiPred


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ("factory", "retails", "indi")

    def validate(self, attrs):
        link_factory = attrs.get("factory")
        link_retails = attrs.get("retails")
        link_indi = attrs.get("indi")

        links_vendor = (link_factory, link_retails, link_indi)

        if sum(map(lambda x: x is not None, links_vendor)) != 1:
            assert ValidationError({"error": "Адрес может быть только у одного поставщика"})

        return attrs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("factory", "retails", "indi")

    def validate(self, attrs):
        link_factory = attrs.get("factory")
        link_retails = attrs.get("retails")
        link_indi = attrs.get("indi")

        links_vendor = (link_factory, link_retails, link_indi)

        if sum(map(lambda x: x is not None, links_vendor)) != 1:
            assert ValidationError({"error": "Продукт может быть только у одного поставщика"})

        return attrs


class FactorySerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=False)
    product = ProductSerializer(read_only=False)

    class Meta:
        model = Factory
        fields = "__all__"

    def create(self, validated_data):
        contact = validated_data.pop("contact")
        product = validated_data.pop("product")

        with transaction.atomic():
            instance = self.Meta.model.objects.create(**validated_data)

            data = {}
            if self.Meta.model is Factory:
                data["factory"] = instance
            elif self.Meta.model is RetailsNet:
                data["retails"] = instance
            elif self.Meta.model is IndiPred:
                data["indi"] = instance
            else:
                raise ValidationError({"error": "Ошибка сохранения поставщика"})

            Contact.objects.create(**contact, **data)
            Product.objects.create(**product, **data)

        return instance


class RetailSerializer(FactorySerializer):
    class Meta:
        model = RetailsNet
        fields = "__all__"

    def validate(self, attrs):
        link_factory = attrs.get("factory")
        link_retails = attrs.get("retails_net")
        link_indi = attrs.get("indi_pred")

        links_vendor = (link_factory, link_retails, link_indi)

        if sum(map(lambda x: x is not None, links_vendor)) != 1:
            assert ValidationError({"error": "Связь может быть только с одним поставщиком"})

        return attrs


class IndividualSerializer(RetailSerializer):
    class Meta:
        model = IndiPred
        fields = "__all__"
