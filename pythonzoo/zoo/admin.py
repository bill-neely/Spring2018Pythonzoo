from django.contrib import admin

from .models import Zoo, Exhibit, ExhibitNeighbor, Animal

# Register your models here.


class ZooAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'logoFileName')

admin.site.register(Zoo, ZooAdmin)

class ExhbitNeighborInline(admin.TabularInline):
	model = ExhibitNeighbor
	fk_name = 'fromExhibit'

class ExhibitAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'getZooName', 'getNumberOfAnimals')
	inlines = [ExhbitNeighborInline]

admin.site.register(Exhibit, ExhibitAdmin)

class ExhibitNeighborAdmin(admin.ModelAdmin):
	list_display = ('id', 'fromExhibit', 'direction', 'toExhibit')

admin.site.register(ExhibitNeighbor, ExhibitNeighborAdmin)

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'exhibit', 'imageFileName', 'soundFileName')

admin.site.register(Animal, AnimalAdmin)
