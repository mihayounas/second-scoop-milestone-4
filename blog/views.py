from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth import authenticate
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from .models import Post, Reservation, Contact, Profile, Comment
from .forms import CommentForm, Booking, ContactForm, PostForm
import datetime
from django.urls import reverse_lazy
from django.contrib import messages


class PostList(generic.ListView):
    """
    This view is showing the list of posts on the blog
    giving information about each post.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    After clicking on a post this will help diplaying
    all the post details allwing you to add a comment 
    or like.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=False).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },

        )

    def get_queryset(self):
        user = self.request.user


class DeleteComment(DeleteView):
    """
    A view to delete a reservations.
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('post_view')


class PostLike(View):
    """
    Allowing post likes
    """

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(CreateView):
    """
    A view to add a new post.
    """
    model = Post
    template_name = 'new_posts.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        """ adding the username automatically for the reservation """
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView):
    """
    A view to edit and update a post.
    """
    model = Post
    template_name = 'update_posts.html'
    fields = ['title', 'featured_image', 'content', ]


class DeletePost(DeleteView):
    """
    A view to delete a post.
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_view')


def homepage(request):
    """ A view to go to the homepage page """
    return render(request, './homepage.html')


def menu(request):
    """ A view to go to the menu page """
    return render(request, './menu.html')


def thanks(request):
    """ A view to go to the thanks page """
    return render(request, './thank_you.html')


class ReservationRequest(CreateView):
    """
    A view which will create reservation form page 
    to request a resrvations,this will send a reservation
    to admin for approval.
    """
    model = Reservation
    form_class = Booking
    template_name = 'reservations.html'

    # Adding the user here - Ger

    def form_valid(self, form):
        """ adding the username automatically for the reservation """
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReservationsView(CreateView):

    model = Reservation
    template_name = 'reservations_details.html'
    fields = ['date', 'event', 'approved', 'message']


class ReservationsList(generic.ListView):
    """
    This view will display all the reservations for a current
    user and offering details about each reservations.
    """
    model = Reservation
    template_name = "reservations_details.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(user=user)


class UpdateReservations(UpdateView):
    """
    A view to edit and update a reservations.
    """
    model = Reservation
    template_name = "update_reservation.html"
    fields = ['phone', 'date', 'event', 'message']


class DeleteReservations(DeleteView):
    """
    A view to delete a reservations.
    """
    model = Reservation
    template_name = 'delete_reservations.html'
    success_url = reverse_lazy('reservations_view')


class ReservationsViewDetails(DetailView):
    model = Reservation
    template_name = 'reservation_view_details.html'
    fields = ['phone', 'date', 'event', 'message']

    def get_id(self, request):
        user = self.request.user
        reservation = Reservation.objects.filter(id=id)


class ContactAdmin(CreateView):
    """
    A view to display contact form for messages to admin.
    """
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        """ adding the username automatically for the message """
        form.instance.client = self.request.user
        return super().form_valid(form)


class MessagesList(generic.ListView):
    """
    A view to display  the created messages to user.
    """
    model = Contact
    template_name = "message_view.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(user=user)


class UpdateMessages(UpdateView):
    """
    A view to edit and update a message.
    """
    model = Contact
    template_name = "edit_messages.html"
    fields = ['name', 'email', 'message']


class DeleteMessages(DeleteView):
    """
    A view to delete messages.
    """
    model = Contact
    template_name = 'delete_messages.html'
    success_url = reverse_lazy('message_list')


def error404_view(request, exception):
    return render(request, 'error.html', status=404)


def error500_view(request):
    return render(request, 'error.html', status=500)


def admin(condition):
    return redirect('admin:index')
