from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe

GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
)


def profile_upload_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT / profile / user_<id>_username / <filename>"""
    return f'profile/{instance.user.id}_{instance.user.username}/{filename}'


class ProfileManager(models.Manager):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = ((GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), )

    def males(self):
        return self.all().filter(gender=self.GENDER_MALE)

    def females(self):
        return self.all().filter(gender=self.GENDER_FEMALE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signature = models.TextField(max_length=500, blank=True)
    # nationality = models.CharField(max_length=2, choices=COUNTRIES)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=ProfileManager.GENDER_CHOICES)
    image = models.ImageField(default='profile/default.jpg', upload_to=profile_upload_path)
    website = models.URLField(default='', blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    # gender = models.IntegerField(choices=GENDER_CHOICES)
    objects = ProfileManager()

    def greet(self):
        return {
            ProfileManager.GENDER_MALE: 'Hi, boy',
            ProfileManager.GENDER_FEMALE: 'Hi, girl.'
        }[self.gender]

    def image_tag(self):
        return mark_safe(f'<img src="{self.get_image()}" width="50" height="50" />')

    def get_image(self):
        if not self.image:
            return '/media/profile/default.jpg'
        return self.image.url


    def __str__(self):
        return f'{self.user.username} Profile'

    def last_login(self):
        return self.user.last_login

    def date_joined(self):
        return self.user.date_joined

    def get_phone_number(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse("main:user-profile", kwargs={"user": self.user.username})

    def get_image_upload_url(self):
        return reverse("main:image_upload", kwargs={"user": self.user.username})

    image_tag.short_description = 'Avatar'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # user_profile =


post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
