from django.http import JsonResponse, HttpResponse

from employees.models import Employee
from department.models import Department
from decorators import POST, deserialize_body, body_has

@POST
@deserialize_body
@body_has([
  'fullname',
  'department_id',
  'position',
  'email',
  'telephone'
])
def add(request):
  body = request.deserialized

  try:
    try:
      department = Department.objects.filter(pk=body['department_id'])

      if (len(department) != 0):
        new_empl = Employee(
          fullname=body['fullname'],
          department=department[0],
          position=body['position'],
          email=body['email'],
          telephone=body['telephone'],
        )

        new_empl.save()

        return JsonResponse({ 'ok': True })
      else:
        return JsonResponse({ 'ok': False, 'message': 'No such department' }, status=400)
    except:
      return HttpResponse('Internal Server Error', status=500)
  except:
    return HttpResponse('Internal Server Error', status=500)