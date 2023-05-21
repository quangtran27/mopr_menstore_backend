from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields = ( 'id',  'user_id', 'order_id', 'title', 'body', 'is_checked', 'created' )
    def get_created(self, obj):
        return obj.created.strftime("%H:%M %d-%m-%Y")
    
