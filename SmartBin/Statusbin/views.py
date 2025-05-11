

# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Bin

def dashboard(request):
    selected_area = request.GET.get('area')
    if selected_area:
        bins = Bin.objects.filter(area=selected_area)
    else:
        bins = Bin.objects.all()

    areas = Bin.objects.values_list('area', flat=True).distinct()
    return render(request, 'dashboard.html', {
        'bins': bins,
        'areas': areas,
        'selected_area': selected_area
    })




def unlock_bin(request, bin_id):
    if request.method == 'POST':
        bin = get_object_or_404(Bin, id=bin_id)
        # 🛠️ Here you can later add code to trigger the actual unlock via sensors (like GPIO/Arduino API)
        print(f"Unlocked bin at {bin.location}")
        return redirect(request.META.get('HTTP_REFERER', '/'))
