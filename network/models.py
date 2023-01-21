from django.db import models


class Vendor(models.Model):
    class Type(models.IntegerChoices):
        FACTORY = 0, "Завод"
        RETAIL_NET = 1, "Розничная сеть"
        INDIVIDUAL_PR = 2, "Индивидуальный предприниматель"

    title = models.CharField(max_length=50)
    type = models.PositiveIntegerField(choices=Type.choices)
    vendor = models.OneToOneField("self", on_delete=models.PROTECT, null=True, blank=True)
    indebtedness = models.DecimalField(decimal_places=2, max_digits=25, default=0.00)
    hierarchy = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.SmallIntegerField()

    vendor = models.OneToOneField("Vendor", on_delete=models.PROTECT)


class Product(models.Model):
    title = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey("Vendor", on_delete=models.PROTECT, related_name="products")
