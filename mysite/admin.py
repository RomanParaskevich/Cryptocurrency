from django.contrib import admin
from .models import Advertising, Coins, Header, MainInfo, SocialNetworks, Footer, InlineFooter, Subscribers, Mail, Sender


admin.site.register(Header)

admin.site.register(Advertising)

admin.site.register(Coins)

admin.site.register(MainInfo)

admin.site.register(SocialNetworks)

admin.site.register(Subscribers)

admin.site.register(Mail)

admin.site.register(Sender)


class InlineFooterInline(admin.TabularInline):
    model = InlineFooter
    fk_name = 'footer'


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    inlines = [InlineFooterInline]
