from django.contrib import admin
from .models import Contact
from .forms import ContactForm


class ContactAdmin(admin.ModelAdmin):

    model = Contact
    add_form = ContactForm
    list_display = (
            "name",
            "email",
            "message"
            )

admin.site.register(Contact, ContactAdmin)


