import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Actor,Director,Movie,Movie_Cast,Reviewer,Generes,Movie_Genres

class ActorsType(DjangoObjectType):
    class Meta:
        model=Actor
        fields=("act_id","act_fname","act_lname","act_gender")

class DirectorsType(DjangoObjectType):
    class Meta:
        model=Director
        fields=("dir_id","dir_fname","dir_lname")

class MoviesType(DjangoObjectType):
    class Meta:
        model=Movie
        fields=("mov_id","mov_name","mov_year","mov_dt_rel", "mov_rel_country","mov_time")

class Movie_CastType(DjangoObjectType):
    class Meta:
        model=Movie_Cast
        fields=("act_id","role")

class ReviewerType(DjangoObjectType):
    class Meta:
        model=Reviewer
        fields=("rev_id","rev_name")

class GeneresType(DjangoObjectType):
    class Meta:
        model=Generes
        fields=("gen_id","gen_name")

class Query(graphene.ObjectType):
    all_actors=DjangoListField(ActorsType)
    all_directors=DjangoListField(DirectorsType)
    all_movies=DjangoListField(MoviesType)
    all_movie_cast=DjangoListField(Movie_CastType)
    all_review=DjangoListField(ReviewerType)
    all_generes=DjangoListField(GeneresType)
    

    def resolve_all_actors(root,info):
        return Actor.objects.all()

    def resolve_all_directors(root,info):
        return Director.objects.all()

    def resolve_all_movies(root,info):
        return Movie.objects.all()

    def resolve_all_movies(root,info):
        return Movie_Cast.objects.all()

    def resolve_all_review(root,info):
        return Reviewer.objects.all()

    def resolve_all_generes(root,info):
        return Generes.objects.all()







schema=graphene.Schema(query=Query)