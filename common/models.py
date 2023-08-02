from django.db import models

class CommonFieldsModel(models.Model):
	'''
	Common model to inherit in models with same fields
	'''
	created_at = models.DateTimeField(auto_now_add=True)# A timestamp representing when this object was created.
	updated_at = models.DateTimeField(auto_now=True)# A timestamp reprensenting when this object was last updated.
	is_active = models.BooleanField(default=True)

	class Meta:
		abstract = True
		ordering = ['-created_at', '-updated_at']


class UserGroup(models.Model):
    """
    Model to store name pf the classes
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name