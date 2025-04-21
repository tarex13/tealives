# from django.conf import settings
# from django.contrib.auth.hashers import check_password
# from custom_user.models import CustomUser
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
# class CustomUserBackend:
	
# 	def authenticate(self,request,phone=None,password=None):
# 		if phone and password:
# 			try:
# 				user = CustomUser.objects.get(phone=phone)
# 				if check_password(password,user.password):
# 					if user.is_active:
# 						return user
# 			except CustomUser.DoesNotExist:
# 				return None
# 		return None

# 	def get_user(self,user_id):
# 		try:
# 			return CustomUser.objects.get(pk=user_id)
# 		except CustomUser.DoesNotExist:
# 			return None