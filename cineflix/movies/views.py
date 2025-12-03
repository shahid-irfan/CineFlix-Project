from django.shortcuts import render,redirect

from django.views import View

from .models import Movie,IndusrtyChoices,GenreChoices,ArtistChoices,LanguageChoices,CertificationChoices

from .forms import MovieForm

from django.db.models import Q
# q is used for complex queries
#  complex queries ennathu oru fieldil allaathathilum search cheyyan vendi use cheyunne

from django.utils.decorators import method_decorator
# class based viewil decorator use cheyyan vendi ith use cheyunne

from authentication.permissions import permitted_user_roles
# import cheythath authenticationil ninn means permissions.py fileil ninn

# Create your views here.

class HomeView(View):

    template = 'home.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'Home'}

        return render(request,self.template,context=data)
    
class MoviesListView(View):

    template = 'movies/movie-list.html'

    def get(self,request,*args,**kwargs):

        # print(request.GET)
        # backendill searchbarill ullath kittan vendi   terminalill kittum

        query = request.GET.get('query')

        movies = Movie.objects.filter(active_status=True)
        # first movies variable wrk aakum active status true aakalar werk aakum..pinne query wrkk aakum 
        # if wrk aakum.....if ulla results movies kond iddum 

        #  movies kazhinjitt annu filter cheyunnath   
        if query :

            movies = movies.filter(Q(name__icontains=query)|
                                Q(description__icontains=query)|
                                Q(industry__name__icontains=query)|
                                Q(certification__icontains=query)|
                                Q(genre__name__icontains=query)|
                                Q(artist__name__icontains=query)|
                                Q(language__name__icontains=query)|
                                Q(tags__icontains=query)
                                ).distinct()
                                
                    # .active status true ayyeeirikkum
                    #  # moviename ,industry,des keyword
                    # __contains orm query.....s,q,we vech search cheyumbol kittan vendi
                    # __contains case senstive annu  so namal __icontains use cheyum..insenstive

                    # movies = movies.filter(name__contains=query,description__contains=query) koduthat
                    # , itt pookumbol niiint pookum   ath matan annu 'Q' cheyunnath   from django db import kodukkannum 
        
        
        data = {'page':'movies','movies':movies,'query':query}
        # (query:query) kodukkunnath search cheythath aaa serach barill kanan vendi
        # base html poye search avide value passs cheyannum {{}}

        return render(request,self.template,context=data)
    

# class MovieCreateView(View):
    

#     def get(self,request,*args,**kwargs):

        # indusrtyChoices=IndusrtyChoices

        # genrechoices=GenreChoices

        # artistchoices = ArtistChoices

        # languagechoices=LanguageChoices

        # certificatechoices = CertificationChoices 
        # form = MovieForm()
        # # object name = form/class 

        # data={
            
        #     'page':'Create Movie',
        #     'form' : form ,
            # frontendill konduvaran vendi namal key

              
            # 'industrychoices':indusrtyChoices,

            # 'genrechoices':genrechoices,

            # 'artistchoices':artistchoices,

    #         # 'languageschoices':languagechoices,

    #         # 'certificatechoices':certificatechoices
  

    #     return render (request,'movies/movie-create.html',context=data)
    
    # def post(self,request,*args,**kwargs):

    #     form = MovieForm(request.POST,request.FILES)
    #     # object class = enn koduth... request.files koduthath images undakkill mataram

    #     if form.is_valid():
    #         #true allakill false kannikkum.. is valid use cheryumnbol  "boolean operator"

    #         form.save()
    #         #last ulla 3 code matatm matti...object creationinnn vendi

            
        # movie_data=request.POST------------------------------------------------->

        # name=movie_data.get('name')                        [  ithrayum  namal form vech cheythu..appo code reduce cheythu  ] 
        # photo=request.FILES.get('photo')

        # description=movie_data.get('description')

        # release_date=movie_data.get('release_date')

        # runtime=movie_data.get('runtime')

        # certification=movie_data.get('certification')

        # industry = movie_data.get('industry')

        # languages = movie_data.get('languages')

        # genre = movie_data.get('genre')

        # artist = movie_data.get('artists')

        # video = movie_data.get('video')

        # tags = movie_data.get('tags')

        # # print(name,photo,description,release_date,runtime,certification,industry,languages,genre,artist,video,tags)
        
        # Movie.objects.create(name=name,

        #                      photo=photo,

        #                      description=description,

        #                      release_date=release_date,

        #                      industry=industry,

        #                      runtime=runtime,

        #                      certification=certification,

        #                      genre=genre,

        #                      artist = artist,

        #                      video=video,

        #                      tags=tags,

        #                      languages=languages)------------------------------------------->



# ------------------------------------------------------------------------------need to complete the code  12(7/10)

            # return redirect('movie-list')



@method_decorator(permitted_user_roles(['Admin']),name='dispatch')
# method decorator use cheyyunnath class based viewil aanu...classil ella methodsinum apply cheyyan vendi dispatch enn kodukkunnu

class MovieCreateView(View):
    
    form_class = MovieForm

    template = 'movies/movie-create.html'

    def get(self,request,*args,**kwargs):

        form  = self.form_class()

        data = {'page':'Create Movie',
                'form':form}

        return render(request,self.template,context=data)
    
    
    def post(self,request,*args,**kwargs):
        # edit cheythitt submit cheyan annu post method use cheyunne

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('movie-list')
        
        
                
        data = {'form':form,'page' : 'create Movie'}

        return render(request,self.template,context=data)
    




    
#  -------------implementing with id----------------------

# class MovieDetailsView(View):

#     template = 'movies/movie-details.html'

#     def get(self,request,*args,**kwargs):
        
#         id = kwargs.get('id')
#         # keyword args dict datatype ayeeeitt varum...key annu id

#         movie = Movie.objects.get(id=id)
#         # object = class
#         # url query

#         data = {'movie':movie,'page':movie.name}
#         #id context vech passs cheyannum
#         # urlill peru varan annu ith pass cheythe    

#         return render(request,self.template,context=data)
#         # context=data kodukkumbol namaku data click cheyumbol varum




# ------------------implementing with uuid------------------------

class MovieDetailsView(View):

    template = 'movies/movie-details.html'

    def get(self,request,*args,**kwargs):
        
        uuid = kwargs.get('uuid')
        # keyword args dict datatype ayeeeitt varum...key annu id

        movie = Movie.objects.get(uuid=uuid)
        # object = class
        # url query

        data = {'movie':movie,'page':movie.name}
        #id context vech passs cheyannum
        # urlill peru varan annu ith pass cheythe    

        return render(request,self.template,context=data)
        # context=data kodukkumbol namaku data click cheyumbol varum

@method_decorator(permitted_user_roles(['Admin']),name='dispatch')  
class MovieEditView(View):

    form_class = MovieForm

    template = 'movies/movie-edit.html'

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie= Movie.objects.get(uuid=uuid)

        form = self.form_class( instance=movie)
        # already dbmsill record und..aaa record form classill instance ayee pass aakum (movie)
        # appo form class eduth vekkannum...record eduth object via pass cheyannum..plus oru parameter pass cheyum (uuid)
        # ----record kudukkym----ath form kodukkum
        # uuid and movie form create cheythitt create cheythath annu

        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

         uuid = kwargs.get('uuid')

         movie= Movie.objects.get(uuid=uuid)

         form = self.form_class(request.POST,request.FILES,instance=movie)
        # img form class und + edit cheyan und.. record ethann annu enn kodukkannum,
        # athannum nammal [post] akath uuid and movie kodukkunne
       

         if form.is_valid():
            #  form valid anno enn check cheyan vendi annu 
             
             form.save()

             return redirect('movie-details',uuid=uuid)
                # thirich movie detailslott ponnum and uuid koode und

         data = {'form':form,'page':movie.name}
            # etannu error enn ariyannum athinn annu

         return render(request,self.template,context=data)


@method_decorator(permitted_user_roles(['Admin']),name='dispatch')

class MovieDeleteView(View):

    def get(self,*args,**kwargs):

        
        uuid = kwargs.get('uuid')

        movie= Movie.objects.get(uuid=uuid)

        # movie.delete()
            # hard delete

        # -------------SOFT DELETE---------------------
        movie.active_status = False

        movie.save()
        
        return redirect('movie-list')
    
    # athiyam aaa record edukkanum enitt deleta cheyannum

