from django.contrib import admin
from django.utils.html import format_html

from .models import *

# Register your models here.


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1
    exclude = ('media_type',)  # Exclude media_type field from form
    readonly_fields = ('preview',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'preview',"file_url")

    def file_url(self,obj):
        return obj.file.url
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_medias','get_price')
    readonly_fields = ('post_date', 'update_date')
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [PriceInline,MediaInline]
    prepopulated_fields = {'slug': ('name',)}

    def display_medias(self, obj):
        html = '<img src="{}" style="max-width: 50px; max-height: 50px;" />'
        return format_html(''.join(html.format(media.file.url) for media in obj.media_set.all() if media.media_type == "Image" ))
    display_medias.short_description = 'Medias'

    def get_price(self,obj):
        price = Price.objects.filter(listing=obj).first()
        if price:
            return "{}/{}".format(price.saleprice, price.unit.symbol)
        else:
            return 'N/A'
    get_price.short_description = 'Price/Unit'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','display_medias','get_price')
    readonly_fields = ('post_date', 'update_date')
    inlines = [PriceInline,MediaInline]
    prepopulated_fields = {'slug': ('name',)}


    def display_medias(self, obj):
        html = '<img src="{}" style="max-width: 50px; max-height: 50px;" />'
        return format_html(''.join(html.format(media.file.url) for media in obj.media_set.all() if media.media_type == "Image"))
    display_medias.short_description = 'Medias'

    def get_price(self,obj):
        price = Price.objects.filter(listing=obj).first()
        if price:
            return "{}/{}".format(price.saleprice, price.unit.symbol)
        else:
            return 'N/A'
    get_price.short_description = 'Price/Unit'


@admin.register(Currency)
class CurrecyAdmin(admin.ModelAdmin):
    list_display = ('name','symbol','code')


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display=('name','symbol','unit_type','conversion_factor')


admin.site.register([
    # Listing
 ])