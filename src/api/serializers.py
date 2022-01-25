from rest_framework import serializers
from ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    def get_owner(self, obj):
        return {
            "username": obj.person.username,
            "first_name": obj.person.first_name,
            "last_name": obj.person.last_name,
        }

    owner = serializers.SerializerMethodField("get_owner")

    class Meta:
        model = Ticket
        fields = '__all__'
