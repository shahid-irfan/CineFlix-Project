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
    NIVIN_PAULY='Nivinpauly','Nivinpauly'

class LanguageChoices(models.TextChoices):

    MALAYALAM ='Malayalam','Malayalam'
    ENGLISH = 'English','English'
    HINDI = 'Hindi','Hindi'
    TAMIL = 'Tamil','Tamil'
    TELUGU = 'Telugu','Telugu'
    KANADA = 'Kanada','Kanada'


# thazhe koduthath ellam models annu class ayeeiittt

class Industry(BaseClass):

    name=models.CharField(max_length=50)

    class Meta:

        verbose_name='Industries'

        verbose_name_plural='Industries'

    def __str__(self):

        return f'{self.name}'
    
class Genre(BaseClass):

    name=models.CharField(max_length=50)

    class Meta:

        verbose_name='Genre'

        verbose_name_plural='Genre'

    def __str__(self):

        return f'{self.name}'
    
class Artist(BaseClass):

    name=models.CharField(max_length=50)

    dob = models.DateField()

    description = models.TextField()

    class Meta:

        verbose_name='Artist'

        verbose_name_plural='Artist'

    def __str__(self):

        return f'{self.name}'
    
class languages(BaseClass):

    name=models.CharField(max_length=50)

    class Meta:

        verbose_name='languages'

        verbose_name_plural='languages'

    def __str__(self):

        return f'{self.name}'
    

class Movie(BaseClass):
    # inherites the baseclass (base classill models und.. models also inheritance  "multilevel inheritance")
    #namal industry,certification okke ivde declare cheythitt namal purth class ezhitum

    name=models.CharField(max_length=50)

    description= models.TextField()
    
    photo = models.ImageField(upload_to='movies/banner-images')
     #jpeg.png files matarme allowed aaku


    release_date = models.DateField()

    # industry = models.CharField(max_length=20,choices=IndusrtyChoices.choices)\

    

    industry = models.ForeignKey('Industry',on_delete=models.CASCADE)
        # on delete--foreign key kodukkumbol kodkkum.. Industry is connected to mollywood is connected to empuran
        # delete cheythal nth sambavikkannum paranj kodukkum athoin  annu models.cascade
        # aaa industry ulla moives poovan annu cascade kodukkune

        # set_null industy pookumbol null kanikkan vendi
    

    runtime = models.TimeField()

    certification = models.CharField(max_length=10,choices=CertificationChoices.choices)

    # genre = MultiSelectField(choices=GenreChoices.choices)
    # multiselect field kodukkumbol max lenght=30 enn kodukkan pattilla 

    genre = models.ManyToManyField('Genre')

    # artist = MultiSelectField(choices=ArtistChoices.choices)

    artist = models.ManyToManyField('Artist')

    video = EmbedVideoField()

    tags = models.CharField()

    # languages = MultiSelectField(choices=LanguageChoices.choices)

    languages = models.ManyToManyField('languages')

    #multiple field vekkan django pettilla..
    #python has for package for multiple field ----------"pip install django-multiselectfield"--------------------------------

# embedded (youtube videos add aakan vendi)---- pip install django-embed-video
    
    class Meta :

        verbose_name = 'Movies'

        verbose_name_plural='Movies'

    def __str__(self):

        return f'{self.name}'   
    
    




# pip install pillow                                          uses of pillow
#   The pip install pillow command is used to install the Pillow library, which is an actively maintained fork of the Python 
#   Imaging Library (PIL). Pillow provides extensive capabilities for image processing and manipulation in Python. 
 
#-------python manage.py makemigrations  ----->   to create new migration files based on the changes made to your Django models.'
#migrate
 
# ----python manage.py migrate----

# create superuser-----> py manage.py createsuperuser-----
#   user:admin
#   pass:admin

#main pjt -----> cd .\cineflix project


# ------- 1 --- "" -------------- make migrations kodukkumbol set aakunne reetiyil






#  eee  models thamil relation vennom
#  types of relationship
#      1 one to one relationship  
#      2. foreign key
#      3.many to many

    # industry---foreign key
    # CertificationChoices--- manyto many
    # genre -- many to many
    # artist --- many to many
    # language -- many to many