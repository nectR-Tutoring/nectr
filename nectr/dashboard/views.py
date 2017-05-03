from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/complete_profile.html"


def student_dashboard(request):
    objects = ""
    objects.username = request.user.username
    objects.transactions = ""

    return render(request, 'dashboard/Student_Dashboard.html', {'objects': objects})
