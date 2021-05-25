from django.contrib import admin
from . import models


class AuthorsAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'first_name',
        'last_name',
        'biography',
        'created',
        'updated'
    ]


class GenresAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'genre'
    ]


class PublishersAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'publisher'
    ]


class SeriesAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'count_series'
    ]


class AnnotationAdmin(admin.ModelAdmin):
    list_display = [
        'annotation'
    ]


admin.site.register(models.Authors, AuthorsAdmin)
admin.site.register(models.Genres, GenresAdmin)
admin.site.register(models.Publishers, PublishersAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Annotation, AnnotationAdmin)

