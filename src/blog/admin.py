from django.contrib import admin

from blog.models import Postagem, Tag, PostTag

class TagsInline(admin.TabularInline):
    model = PostTag
    extra = 2

class PostagemAdmin(admin.ModelAdmin):
    list_display = ['autor', 'titulo', 'pronto', 'curtidas', 'categoria', 'qtd_tags', 'tags_texto']
    inlines = (TagsInline,)
    actions = ['set_prontos',]
    search_fields = ['titulo', 'texto']
    list_filter = ['pronto', 'categoria', 'tags']

    def qtd_tags(self, obj):
        qtd = len(obj.tags.all())
        return qtd

    def tags_texto(self, obj):
        tags = obj.tags.all()
        resp = ''
        for tag in tags:
            resp = resp + ', ' + tag.texto

        return resp[2:]

    @admin.action(description='Marcar como prontos para publicar')
    def set_prontos(self, request, queryset):
        queryset.update(pronto=True)

# Register your models here.
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Tag)