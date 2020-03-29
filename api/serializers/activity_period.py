
from dance_app.models import activity_period,user
from rest_framework import serializers



class activity_period_infoSerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model = activity_period
		fields = ['start_time', 'end_time']




class UserSerializer(serializers.ModelSerializer):
	activity_periods = activity_period_infoSerializer(many=True, read_only=True)
	real_name = serializers.CharField(source='user.real_name')
	tz = serializers.CharField(source='user.tz')
	
	class Meta:
		model = user
		fields = ['real_name', 'tz','activity_periods']






    


