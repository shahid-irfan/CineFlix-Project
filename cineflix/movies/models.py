from django.db import models

import uuid

from multiselectfield import MultiSelectField

from embed_video.fields import EmbedVideoField
# Create your models here.

class BaseClass(models.Model):

    uuid = models.UUIDField(unique=True,default=uuid.uuid4)
    # uuid gernerates unique hexadecimal numbers for avoid data manipulation in urls
    # 'default' --  gives because values onnum koduthillakill default ayee kodukkan vendi
    # uuid4() is not given function call because ath thodakathil varanda..

    active_status = models.BooleanField(default=True)
    # active status is for the soft delete true annakill up false annakill delete ayee kidakkum

    created_at = models.DateTimeField(auto_now_add=True)
    # auto now == updated aaakum
    # auto now add = time created cheythal maran padilla..no changes

    updated_at = models.DateTimeField(auto_now=True)

    class Meta :

        abstract = True

class IndusrtyChoices(models.TextChoices):
  
    # choice = 'key','value'
    Mollywood = 'Mollywood','Mollywood'
    Hollywood = 'Hollywood','Hollywood'
    Bollywood = 'Bollywood','Bollywood'
    Tollywood = 'Tollywood','Tollywood'

class CertificationChoices(models.TextChoices):

    A = 'A','A'
    U = 'U','U'
    UA = 'U/A','U/A'
    S = 'S','S'

class GenreChoices(models.TextChoices):
    ACTION='Action','Action'
    ROMANTIC='Romantic','Romantic'
    THRILLER='Thriller','Thriller'
    COMEDY='Comedy','Comedy'
    HORROR='Horror','Horror'

class ArtistChoices(models.TextChoices):

    MOHANLAL='Mohanlal','Mohanlal'
    MAMMOOTTY='Mammooty','Mammooty'

class LanguageChoices(models.TextChoices):

    MALAYALAM ='Malayalam','Malayalam'
    ENGLISH = 'English','English'
    HINDI = 'Hindi','Hindi'
    TAMIL = 'Tamil','Tamil'
    TELUGU = 'Telugu','Telugu'
    KANADA = 'Kanada','Kanada'


class Movie(BaseClass):
    # inherites the baseclass (base classill models und.. models also inheritance  "multilevel inheritance")
    #namal industry,certification okke ivde declare cheythitt namal purth class ezhitum

    name=models.CharField(max_length=50)

    description= models.TextField()
    photo = models.ImageField(upload_to='movies/banner-images')

    release_date = models.DateField()

    industry = models.CharField(max_length=20,choices=IndusrtyChoices.choices)

    runtime = models.TimeField()

    certification = models.CharField(max_length=10,choices=CertificationChoices.choices)

    genre = MultiSelectField(choices=GenreChoices.choices)
    # multiselect field kodukkumbol max lenght=30 enn kodukkan pattilla 

    artist = MultiSelectField(choices=ArtistChoices.choices)

    video = EmbedVideoField()

    tags = models.CharField()

    languages = MultiSelectField(choices=LanguageChoices.choices)

    #multiple field vekkan django pettilla..
    #python has for package for multiple field ----------"pip install django-multiselectfield"--------------------------------

# embedded (youtube videos add aakan vendi)---- pip install django-embed-video
    # 

    class Meta :

        verbose_name = 'Movies'

        verbose_name_plural='Movies'

    def __str__(self):

        return f'{self.name}'


# pip install pillow

#-------python manage.py makemigrations  ----->   to create new migration files based on the changes made to your Django models.'
#migrate
 
# ----python manage.py migrate----

# create superuser-----> py manage.py createsuperuser-----
#   user:admin
#   pass:admin

# -------1---""-------------- make migrations kodukkumbol set aakunne reetiyill







    

