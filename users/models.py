from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):    
    
    def create_user(self, email, full_name, username, password, **extra_fields):
        try:
            user = self.model(email=email, full_name=full_name, username=username,)
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)  
            user.set_password(password)
            user.is_active = True            
            user.save()            
            return user   
        except Exception as e:            
            print(e)
            
    def create_superuser(self, username, password, **extra_fields):
        try:
            superuser = self.create_user(
                username=username,
                password=password,
                email="admin@admin.com",
                full_name="manager",
                **extra_fields
            )
            superuser.is_admin = True
            superuser.is_superuser = True
            superuser.is_active = True
            superuser.is_staff = True
            superuser.save()
            return superuser
        except Exception as e:
            print(e)


class User(AbstractBaseUser, PermissionsMixin):
    
    """Custom User model definition"""
    
    LOGIN_GITGUB = "github"
    LOGIN_KAKAO = "kakao"
    LOGIN_EMAIL = "email"
    
    LOGIN_CHOICES = (
        (LOGIN_GITGUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_EMAIL, "Email"),
    )
    
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )
    
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    
    email = models.EmailField(max_length=100, null=False)
    full_name = models.CharField(max_length=30, null=False)
    username = models.CharField(max_length=20, unique=True, null=False)
    web_site_url = models.URLField(max_length=150, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    language = models.CharField(max_length=2, default=LANGUAGE_ENGLISH)
    login_method = models.CharField(max_length=6, default=LOGIN_EMAIL)
    
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "username"
    
    objects = UserManager()
    


