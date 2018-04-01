from django.contrib import admin


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
admin.site.register(Move, MoveAdmin)
