from rest_framework import serializers
from base.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        if data['chekin_at'] > data['checkout_at']:
            raise serializers.ValidationError({"checkin_at":"The check-in date must be before the check-out date"})
        return data