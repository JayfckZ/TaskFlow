from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, position, password=None, **extra_fields):
        if not email:
            raise ValueError("O email deve ser fornecido")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, position=position, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, position, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, name, position, password, **extra_fields)


class User(AbstractUser):
    username = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'position']

    objects = UserManager()

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Evita conflito com o nome padrão
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    def __str__(self):
        return self.name
