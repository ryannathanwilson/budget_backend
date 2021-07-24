from rest_framework import serializers
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer): 
 # Currently unused in preference of the below. 
 # """ 
	email = serializers.EmailField( required=True )
	username = serializers.CharField() 
	password = serializers.CharField(min_length=8, write_only=True) 

	class Meta: 
		model = get_user_model() 
		fields = ('email', 'username', 'password', 'id') 
		extra_kwargs = {'password': {'write_only': True}} 
 
	def create(self, validated_data): 
		password = validated_data.pop('password', None) 
		instance = self.Meta.model(**validated_data) 
		# as long as the fields are the same, we can just use this if password is not None: 
		instance.set_password(password) 
		instance.save() 
		return instance
