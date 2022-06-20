from rest_framework import serializers

from .models import Order, Shipment


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "name", "quantity", "weight", "created_at"]


class ShipmentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = [
            "id_reference",
            "order",
            "address",
            "owner_name",
            "owner_email",
            "shipment_date",
            "status",
        ]
