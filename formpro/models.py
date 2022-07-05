from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=150)
    email = models.EmailField(max_length = 254)
    message = models.TextField()
    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('contact_list')

# Ismingiz
# Familiyangiz
# Telefon raqamingiz
# Email manzilingiz
# Xabar yuborish
