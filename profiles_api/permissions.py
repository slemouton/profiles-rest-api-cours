from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	"""allows user to edit theri own profiles"""
	def has_object_permission(self,request,view,obj):
		"""check if user is tryind to edit their own profile"""
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
	"""allow user to updtate their own status"""
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.user_profile.id == request.user.id


