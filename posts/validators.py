from django.core.exceptions import ValidationError 
from posts.models import ScrapUser 

def validate_email(value):
    if ScrapUser.objects.filter(email=value).exists():
        raise ValidationError(
            (f"{value} is taken."),
            params = {'value':value}
        )