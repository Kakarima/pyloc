from django.contrib import admin
from django.utils.text import Truncator

from .models import Category, Agency

admin.site.register(Agency)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'lbl_sample', 'lbl_nb_seats', 'lbl_nb_doors', 'view_description')
    list_filter = ('code', 'label')
    ordering = ('code',)
    search_fields = ('sample',)

    def lbl_sample(self, category):
        return category.sample

    def view_description(self, category):
        return Truncator(category.description).chars(40, truncate='...')

    def lbl_nb_seats(self, category):
        return category.nb_seats

    def lbl_nb_doors(self, category):
        return category.nb_doors

    lbl_sample.short_description = 'Exemple'
    lbl_nb_seats.short_description = 'Nb sièges'
    lbl_nb_doors.short_description = 'Nb portes'
    view_description.short_description = 'Aperçu'

    fieldsets = (
        ('Identité', {'fields': ('code', 'label', 'sample')}),
        ('Confort', {'fields': ('nb_seats', 'nb_doors', 'nb_luggage')}),
        ('Description', {'fields': ('description',)})
    )
