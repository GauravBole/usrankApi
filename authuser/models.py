from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserManager(BaseUserManager):
    """Helpes django work with our custome model"""

    def create_user(self,email,user_id,password = None):
        """Create new user in a system"""

        if not email:
            raise ValueError("user must have enter a emial")

        email = self.normalize_email(email)
        user = self.model(email = email,user_id = user_id)

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,user_id,password):
        """ Create a super user"""

        user = self.create_user(email,user_id,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


class AuthUser(AbstractBaseUser,PermissionsMixin):
    """Represent a "user profile" in our project """

    user_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    birth_date = models.DateField(null=True)
    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        """ convert object to string """

        return self.user_id