from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Show, Rating
# Create your views here.

def index(request):
    latest_show_list = Show.objects.order_by('-pub_date')[:5]
    context = {'latest_show_list': latest_show_list}
    return render(request, 'shows/index.html', context)

def detail(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    return render(request, 'shows/detail.html', {'show' : show})

def rating(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    return render(request, 'shows/results.html', {'show' : show})

# def rate(request, show_id):
#     return HttpResponse("You're rating on show %s." % show_id)
    
def rate(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    try:
        selected_rating = show.rating_set.get(pk=request.POST['rating'])
    except (KeyError, Rating.DoesNotExist):
        # Redisplay the show rating form.
        return render(request, 'shows/detail.html', {
            'show' : show,
            'error_message': "You didn't rate.",
        })
    else:
        selected_rating.rates += 1
        selected_rating.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('shows:rating', args=(show.id,)))