from django.contrib.auth.base_user import BaseUserManager
from api.models import Country

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, birthday, country, phone_number, **other_fields):

        if not email:
            raise ValueError(("The Email must be set"))
        if not country:
            raise ValueError(("Must sent a valid country id"))

        country = Country.objects.get(id=country)

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                            birthday=birthday, country=country, phone_number=phone_number, **other_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, birthday, country, phone_number, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))

        return self.create_user(email, password, first_name, last_name, birthday, country, phone_number, **other_fields)