from django.http import JsonResponse, HttpResponse

from department.models import Department
from company.models import Company
from decorators import POST, deserialize_body, body_has

@POST
@deserialize_body
@body_has([
  'name',
  'companies'
])
def add(request):
  body = request.deserialized

  try:
    try:
      companies = Company.objects.filter(pk__in=body['companies'])

      if (len(companies) != 0):
        new_department = Department(name=body['name'])

        new_department.save()
        new_department.organizations.add(*companies)
        new_department.save()

        return JsonResponse({ 'ok': True })
      else:
        return JsonResponse({ 'ok': False, 'message': 'No such companies' }, status=400)
    except Exception as e:
      e.with_traceback()
      return HttpResponse('Internal Server Error', status=500)
  except Exception as e:
    e.with_traceback()
    return HttpResponse('Internal Server Error', status=500)