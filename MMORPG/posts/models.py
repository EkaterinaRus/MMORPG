from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    # TANKS = 'TN'
    # HEEL = 'HL'
    # DD = 'DD'
    # MERCHANTS = 'MH'
    # GUILDMASTERS = 'GM'
    # QUESTGIVERS = 'QG'
    # BLACKSMITH = 'BS'
    # TANNERS = 'TNR'
    # POTION_MAKERS = 'PM'
    # SPELL_MASTERS = 'SM'
    #
    # NAMES_CATEGORIES = [
    #     (TANKS, 'Танки'),
    #     (HEEL, 'Хилы'),
    #     (DD, 'ДД'),
    #     (MERCHANTS, 'Торговцы'),
    #     (GUILDMASTERS, 'Гилдмастеры'),
    #     (QUESTGIVERS, 'Квестгиверы'),
    #     (BLACKSMITH, 'Кузнецы'),
    #     (TANNERS, 'Кожевники'),
    #     (POTION_MAKERS, 'Зельевары'),
    #     (SPELL_MASTERS, 'Мастера заклинаний')
    # ]

    # NAMES_CATEGORIES = [
    #     ('TN', 'Танки'),
    #     ('HL', 'Хилы'),
    #     ('DD', 'ДД'),
    #     ('MH', 'Торговцы'),
    #     ('GM', 'Гилдмастеры'),
    #     ('QG', 'Квестгиверы'),
    #     ('BS', 'Кузнецы'),
    #     ('TNR', 'Кожевники'),
    #     ('PM', 'Зельевары'),
    #     ('SM', 'Мастера заклинаний')
    # ]

    name_category = models.CharField(max_length=25, unique=True)
    short_name_category = models.CharField(max_length=5, unique=True, null=True)

    def __str__(self):
        return self.name_category

    class Meta:
        ordering = ['id']


class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    content = models.CharField(max_length=255, null=True, blank=True)


class Reply(models.Model):
    text = models.TextField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


