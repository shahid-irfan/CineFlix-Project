from django import forms

from .models import Movie

import os

class MovieForm(forms.ModelForm):
    #----->  control + click on ModelForm  <-----

    class Meta:

        model = Movie

        #fields='__all__'   is used when:-
        # ellam field edukkan vendi namal dunder method
        #kurach fieldeeey ullu enkill namal field cheyum

        exclude = ['uuid','active_status']
        # arookke venda ath venda..
        # orupaaad undakill namal exclude cheyum..

        # dict type...'field':
        # ee typeill ellam namal dict type ayeeirikum 
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter movie name'}) ,
            # attributes..html attr annu kodukkunne(moviecreate html)...athum dict type annu
            #lastill automatically req varum. (class,placeholder,requird). formill model link cheyumbol thanne required varum 
            #output is moive namentey tab is extended

            'photo':forms.FileInput(attrs={'class':'form-control'}),

            'description':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':"Enter movie description"}),

            'release_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            # typedate koduthath detail ayeeitt varan

            'industry':forms.Select(attrs={'class':'form-select'}),
            #outputill options varunnath model ulla data annu.......webill varunnath

            'runtime':forms.TimeInput(attrs={'class':'form-control','type':'time'},format='%H:%M'),

            'certification' : forms.Select(attrs={'class':'form-select'}),
            
            'genre' : forms.SelectMultiple(attrs={'class':'form-select'}),
            # model ulla per annu form varan padillu athey  html varan padillu-------[model--form--html]

            'artist' :  forms.SelectMultiple(attrs={'class':'form-select'}),

            'video' : forms.TextInput(attrs={'class':'form-control','type':'url','placeholder' : 'Enter video URL'}),

            'tags' : forms.Textarea(attrs={'class':'form-control','row':3,'placeholder':'Enter Tags with #'}),

            'languages' : forms.SelectMultiple(attrs={'class':'form-select'})



        }

#--------watch classvideo 7/11  
    def clean(self):

        cleaned_data = super().clean()

        photo = cleaned_data.get('photo')

        if photo and photo.size > 3*1024*1024:

            self.add_error('photo','maximum file size upto 3MB')

            #pixabay----> to get the image 

        # extension = os.path.splitext(photo.name)[1].lower()
        # #filentey extension kidan vendi annu photo.name enn kodukkanne

        # print(extension)

        # if extension not in ['.jpg','.png','.jpeg']:

        #     self.add_error('photo','upload file with extensions jpg,jpeg or png')
        

   