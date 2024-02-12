from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from app.Emailbackend import Emailbackend
from app.models import CustomUser,Register_as_smes,Register_as_startUp

from django.contrib.auth.decorators import login_required

def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request, 'Outside/login.html')


def MESSAGE(request):
    return render(request,'messages.html')


def HOME(request):
    return render(request, 'staff_home.html')



def doLogin(request):
    if request.method == "POST":
        user = Emailbackend.authenticate(request,
                                           username = request.POST.get('username'),
                                           password = request.POST.get('password'),)


        if user!=None:

            login(request,user)
            user_type= user.user_type
            if user_type =='1':
                return redirect('manager_home')
            elif user_type =='2':
                return redirect('staff_home')
            elif user_type=='3':
                return redirect('employee_home')
            else:
                messages.error(request, 'username or password wrong')
                return redirect('login')
        else:

            messages.error(request, 'username or password wrong')
            return redirect('login')
    return HttpResponse(messages)


def doLogout(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }

    return render(request, 'profile.html', context)


def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customeuser = CustomUser.objects.get(id=request.user.id)
            customeuser.first_name = first_name
            customeuser.last_name = last_name
            customeuser.profile_pic = profile_pic
            if password != None and password != "":
                customeuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customeuser.profile_pic = profile_pic
            customeuser.save()
            messages.success(request, "your profile is updated")
            redirect('profile')
        except:
            messages.error(request, 'something wrong')

    return render(request, 'profile.html')


def REGISTER_AS_SMES(request):

    return render(request, 'Outside/register_as_smes.html')


def SAVE_REGISTER_AS_SMES(request):
    if request.method == "POST":
        campany_name = request.POST.get('campany_name')
        campany_type = request.POST.get('campany_type')
        first_name = request.POST.get('first_name')
        father_name= request.POST.get('father_name')
        grand_father_name= request.POST.get('grand_father_name')
        nationality= request.POST.get('nationality')
        region= request.POST.get('region')
        zone= request.POST.get('zone')
        kebele= request.POST.get('kebele')
        house_number= request.POST.get('house_number')
        p_o_box= request.POST.get('p_o_box')
        fax= request.POST.get('fax')
        email= request.POST.get('email')
        capital= request.POST.get('capital')
        tin= request.POST.get('tin')
        registasion_date= request.POST.get('registasion_date')
        vat_no= request.POST.get('vat_no')
        about_title= request.POST.get('about_title')
        field= request.POST.getlist('field')
        proposal= request.FILES.get('proposal')
        registereed = Register_as_startUp(
            campany=campany_name,
            campany_type=campany_type,
            first_name=first_name,
            father_name=father_name,
            grand_father_name=grand_father_name,
            nationality=nationality,
            region=region,
            zone=zone,
            house_number=house_number,
            kebele=kebele,
            p_o_box=p_o_box,
            fax=fax,
            email=email,
            capital=capital,
            tin=tin,
            registasion_date=registasion_date,
            vat_no=vat_no,
            about_title=about_title,
            field=field,
            proposal=proposal,

        )
        registereed.save()
        messages.success(request, '  recorded')
        return redirect('register_as_smes')


def CONFIRM(request):
    return render(request,'includes/confirm.html')


def DASHBOARD(request):
    return render(request,'homepage.html')


def HELP(request):
    return render(request, 'Outside/help.html')


def REGISTER_AS_STARTUP(request):
    return render(request, 'Outside/register_as_smes.html')


def SAVE_REGISTER_AS_STARTUP(request):
    if request.method == "POST":
        campany_name = request.POST.get('campany_name')
        campany_type = request.POST.get('campany_type')
        first_name = request.POST.get('first_name')
        father_name = request.POST.get('father_name')
        grand_father_name = request.POST.get('grand_father_name')
        nationality = request.POST.get('nationality')
        region = request.POST.get('region')
        zone = request.POST.get('zone')
        kebele = request.POST.get('kebele')
        house_number = request.POST.get('house_number')
        p_o_box = request.POST.get('p_o_box')
        fax = request.POST.get('fax')
        email = request.POST.get('email')
        capital = request.POST.get('capital')
        tin = request.POST.get('tin')
        registasion_date = request.POST.get('registasion_date')
        vat_no = request.POST.get('vat_no')
        about_title = request.POST.get('about_title')
        field = request.POST.getlist('field')
        proposal = request.FILES.get('proposal')
        registereed = Register_as_startUp(
            campany=campany_name,
            campany_type=campany_type,
            first_name=first_name,
            father_name=father_name,
            grand_father_name=grand_father_name,
            nationality=nationality,
            region=region,
            zone=zone,
            house_number=house_number,
            kebele=kebele,
            p_o_box=p_o_box,
            fax=fax,
            email=email,
            capital=capital,
            tin=tin,
            registasion_date=registasion_date,
            vat_no=vat_no,
            about_title=about_title,
            field=field,
            proposal=proposal,

        )
        registereed.save()
        messages.success(request, '  recorded')
        return redirect('register_as_startUp')

