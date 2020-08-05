from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .models import BackendProgrammer, Employee


@method_decorator(csrf_exempt, name="dispatch")
class AboutView(View):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        print(request)

        employees = Employee.objects.all()
        backends = BackendProgrammer.objects.all()

        print("1", employees)
        print("2", backends)

        return JsonResponse({}, status=201)
