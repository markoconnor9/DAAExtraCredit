from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Employee
from .models import Shift
from .forms import *
# Create your views here.
def emp(request, employee_key):

    # if the user hit the submit button
    if request.method == "POST":
        

        #change avilabilty button was pressed
        if request.POST.get("changeAvilabity"):
        # getting the users id number 
            idNumber = employee_key
            # validating that a number was inputted and that it exist in the data base
            if(idNumber!=""):
                if Employee.objects.filter(auto_increment_id=idNumber).exists():
                    employee = Employee.objects.get(auto_increment_id = idNumber)
                    employee.availability.all().delete()

                    if "SundayMorning" in request.POST:
                        avilableDuring = Shift(day="Sunday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)
                    #  print(employee.availability.all().delete()) this would remove all the prior schedules



                    if "SundayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Sunday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)

                    if "SundayNight" in request.POST:
                        avilableDuring = Shift(day="Sunday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)

                    if "MondayMorning" in request.POST:
                        avilableDuring = Shift(day="Monday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)

                    if "MondayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Monday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "MondayNight" in request.POST:
                        avilableDuring = Shift(day="Monday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)

                    if "TuesdayMorning" in request.POST:
                        avilableDuring = Shift(day="Tuesday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "TuesdayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Tuesday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "TuesdayNight" in request.POST:
                        avilableDuring = Shift(day="Tuesday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "WednesdayMorning" in request.POST:
                        avilableDuring = Shift(day="Wednesday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "WednesdayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Wednesday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "WednesdayNight" in request.POST:
                        avilableDuring = Shift(day="Wednesday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "ThursdayMorning" in request.POST:
                        avilableDuring = Shift(day="Thursday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "ThursdayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Thursday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "ThursdayNight" in request.POST:
                        avilableDuring = Shift(day="Thursday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "FridayMorning" in request.POST:
                        avilableDuring = Shift(day="Friday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "FridayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Friday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "FridayNight" in request.POST:
                        avilableDuring = Shift(day="Friday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "SaturdayMorning" in request.POST:
                        avilableDuring = Shift(day="Saturday", time="morning")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "SaturdayAfternoon" in request.POST:
                        avilableDuring = Shift(day="Saturday", time="afternoon")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)


                    if "SaturdayNight" in request.POST:
                        avilableDuring = Shift(day="Saturday", time="night")
                        avilableDuring.save()
                        employee.availability.add(avilableDuring)
                        product = request.GET.get('SaturdayNight')
                        print(product)

                else:
                    print("user does not exist")
                
    employees = Employee.objects.all()
    employee = Employee.objects.get(auto_increment_id=employee_key)
    employee_name = employee.name
    return render(request, 'employee.html', {'employee_key':employee_key, 'employee_name':employee_name})




def check(request):
    print("h")
    form = selectForm()
    return render(request, 'check.html', {"form":form})
   #return HttpResponse('Hello world')