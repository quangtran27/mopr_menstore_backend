from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


@api_view(['PUT'])
def update_notification(request, notification_id):
	try:
		notification = Notification.objects.get(id=notification_id)
	except Notification.DoesNotExist:
		return Response({}, status.HTTP_404_NOT_FOUND)
	is_checked = request.POST.get('is_checked')
	if is_checked == 'True':
		notification.is_checked = True
		notification.save()
		return Response(NotificationSerializer(notification).data, status.HTTP_200_OK)
	else:
		return Response({}, status.HTTP_400_BAD_REQUEST)