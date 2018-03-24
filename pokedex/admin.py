from django.contrib import admin
from import_export import resources
from .models import Pokemon
from import_export.admin import ImportExportModelAdmin


class PokemonResource(resources.ModelResource):

    class Meta:
        model = Pokemon
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('dex', 'img', 'name', 'types', 'species', 'height', 'weight')
        #export_order = ('edx_id', 'edx_email')


class PokemonAdmin(ImportExportModelAdmin):
    resource_class = PokemonResource

admin.site.register(Pokemon, PokemonAdmin)


# class edxUserResource(resources.ModelResource):
#     class Meta:
#         model = edxUser
#         skip_unchanged = True
#         report_skipped = True
#         exclude = ('id',)
#         import_id_fields = ('edx_id', 'edx_email', 'edx_name',)
#         #export_order = ('edx_id', 'edx_email')