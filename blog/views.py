from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, ReservationForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

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
        comments = post.comments.filter(approved=True).order_by("-created_on")
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


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def homepage(request):
    """ A view to go to the homepage page """
    return render(request, './homepage.html')


def menu(request):
    """ A view to go to the menu page """
    return render(request, './menu.html')


def reservations(request):
    reservations_form = ReservationForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        if reservations_form.is_valid():
            if request.user.is_authenticated:
                reservation = reservations_form.save(commit=False)
                reservations_form = ReservationForm()
                # optimized the code
                guest = Profile.objects.get(user=request.user)
                reservation.name = guest.name
                reservation.surname = guest.surname
                reservation.phone = guest.phone
                reservation.email = request.user.email
                reservation.save()
            else:
                reservation = reservations_form.save()  # removed duplicate save

        n = reservation.pk
        return redirect('thank_you', n)
    return render(request, 'reservations.html', {'reservations_form': reservations_form})


def thanks(request):
    """ A view to go to the menu page """
    return render(request, './thank-you.html')
