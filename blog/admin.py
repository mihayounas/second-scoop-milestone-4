from django.contrib import admin
from .models import Post, Comment, Reservation, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'event', 'date', 'message')
    search_fields = ('name', 'phone', 'email', 'event', 'date', 'message')
    actions = ['approve_reservation']

    def approve_reservation(self, request, queryset):
        queryset.update(approved=True)
        reservation_form.save()


@admin.register(Contact)
class ContactUs(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    actions = ['respond_message']

    def respond_message(self, request, queryset):
        respond = models.CharField(max_length=100)
        return (respond)
