from django.contrib import admin
from import_export import resources
from .models import Pokemon, Move
from import_export.admin import ImportExportModelAdmin


class PokemonResource(resources.ModelResource):
    class Meta:
        model = Pokemon
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('dex', 'img', 'name', 'types',
                            'species', 'height', 'weight')
        # export_order = ('edx_id', 'edx_email')


class PokemonAdmin(ImportExportModelAdmin):
    resource_class = PokemonResource


class MoveResource(resources.ModelResource):
    class Meta:
        model = Move
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('name', 'element', 'category',
                            'power', 'accuracy', 'pp', 'description',
                            'zmove', 'tm')
        # export_order = ('edx_id', 'edx_email')


class MoveAdmin(ImportExportModelAdmin):
    list_display = ('name', 'element', 'category', 'power', 'accuracy', 'pp')
    resource_class = MoveResource

# Register
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Move, MoveAdmin)
