from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError
from django.db import models

'''
class Type(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name
'''

class Homebrew(models.Model):  # the same as class Rule(Homebrew)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='homebrew_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='homebrew', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # foreign key class?


    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name


class Item(Homebrew):
    class Coinage(models.TextChoices):
        GOLD_CROWNS = 'GC'
        SHILLINGS = 'S'
        PENCE = 'P'


    value = models.IntegerField()
    coinage = models.TextField(choices=Coinage, default='GC')


class Weapon(Item):
    class Stats(models.TextChoices):
        STRENGTH_BASE = 'SB'
        TOGHNESS_BASE = 'TB'
        MAGIC = 'Mag'
        INSANITY_POINTS = 'IP'
        FATE_POINTS = 'FP'
        ATTACKS = 'A'
        MOVEMENT = 'M'
        WOUNDS = 'W'


    primary_stat = models.TextField(choices=Stats, default='SB')
    multiplayer = models.IntegerField()
    modifier = models.IntegerField(blank=True, null=True)
    # list of special qualities?


class Armor(Item):
    class Locations(models.TextChoices):
        HEAD = 'Head'
        BODY = 'Body'
        ARMS = 'Arms'
        LEGS = 'Legs'
        ALL = 'All'


    armor_points = models.IntegerField()
    location_covered = models.TextField(choices=Locations, default='All')


class Career(Homebrew):
    def validate_main_profile(value):
        if value % 5 != 0:
            raise ValidationError(gettext_lazy("%(value)%s is not devisible by 5"), params={"value": value})

    # let main and secondary profile be blank=True, null=True?
    # main profile
    weapon_skill = models.IntegerField(validators=[validate_main_profile])
    balistic_skill = models.IntegerField(validators=[validate_main_profile])
    strength = models.IntegerField(validators=[validate_main_profile])
    toughness = models.IntegerField(validators=[validate_main_profile])
    agility = models.IntegerField(validators=[validate_main_profile])
    intelligence = models.IntegerField(validators=[validate_main_profile])
    will_power = models.IntegerField(validators=[validate_main_profile])
    fellowship = models.IntegerField(validators=[validate_main_profile])
    # secondary profile
    attacks = models.IntegerField()
    wounds = models.IntegerField()
    strength_bonus = models.IntegerField()
    toughness_bonus = models.IntegerField()
    movement = models.IntegerField()
    magic = models.IntegerField()
    insanity_points = models.IntegerField()
    fate_points = models.IntegerField()
    # rest
    skills = models.TextField()
    talents = models.TextField()
    trappings = models.TextField()
    career_entries = models.TextField()
    career_exits = models.TextField()

'''
class Rule(Homebrew):
    pass


class Scenario(Homebrew):
    pass
'''
# needs a shit ton of things or just unmodified Homebrew
