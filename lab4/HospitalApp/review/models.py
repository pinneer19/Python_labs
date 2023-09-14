from django.db import models


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )

    title = models.CharField(max_length=32, help_text="Заголовок")
    stars = models.IntegerField(choices=RATING_CHOICES)
    username = models.CharField(max_length=128, help_text="Логин")
    date = models.DateField(auto_now=True)
    review_text = models.TextField(max_length=256, help_text="Отзыв")