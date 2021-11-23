from typing import Type
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse , HttpResponseRedirect

from parking.models import parking1,parking2,parking3,parking4,overalldata

# Create your views here.


def home(request):

    return render(request,"sigin.html")

def signin(request):
    print("ji")

    if request.user.is_authenticated:
        return render(request,"home.html",{'context':"data from already is_authenticated"})
    else:
        if request.method =="POST":
            un= request.POST["username"]
            pas= request.POST["password"]
            print(un)
            
            user= authenticate(username=un,password=pas)

            if user is not None:
                login(request, user)
                return render(request,"home.html",{'context':"data from already login"})
            else:
                return render(request,"sigin.html",{'context':"Error in username or password"})


    return render(request,"home.html")


def add(request):
    print ("din")
    if request.method == "POST":
        print ("called")
        
        fullname=request.POST["firstname"]
        phonenumber=request.POST["lastname"]
        flatnumber=request.POST["username"]
        pourchno=request.POST["password1"]

        if pourchno == "no" or pourchno == "NO" or pourchno =="No" or pourchno=="nO":
            a=overalldata.objects.create(fullname=fullname,phonenumber=phonenumber,flatnumber=flatnumber,parkingno="",pourchno=pourchno)
            a.save()
            aa = "data of flat " + str(flatnumber) +  " with this pourch number " + str(pourchno) + " added Successfully "
            return render(request,"home.html",{'status1': aa} )
        elif pourchno=="":
                a=overalldata.objects.create(fullname=fullname,phonenumber=phonenumber,flatnumber=flatnumber,parkingno="",pourchno=pourchno)
                a.save()
                aa = "data of flat " + str(flatnumber) +  " with this pourch number " + str(pourchno) + " added Successfully "
                return render(request,"home.html",{'status1': aa} )
        else :
            if int(pourchno) > (100) and int(pourchno) < (174) :

                a=overalldata.objects.create(fullname=fullname,phonenumber=phonenumber,flatnumber=flatnumber,parkingno="p1",pourchno=pourchno)
                a.save()
                aa = "data of flat " + str(flatnumber) +  " with this pourch number " + str(pourchno) + " added Successfully "
                return render(request,"home.html",{'status1': aa} )

            
            elif int(pourchno) >= (201) and int(pourchno) <= (273) :

                a=overalldata.objects.create(fullname=fullname,phonenumber=phonenumber,flatnumber=flatnumber,parkingno="p2",pourchno=pourchno)
                a.save()
                aa = "data of flat " + str(flatnumber) +  " with this pourch number " + str(pourchno) + " added Successfully "
                return render(request,"home.html",{'status1': aa} )


            
            elif int(pourchno) >= (301) and int(pourchno) <= (373) :

                a=overalldata.objects.create(fullname=fullname,phonenumber=phonenumber,flatnumber=flatnumber,parkingno="p3",pourchno=pourchno)
                a.save()
                aa = "data of flat " + str(flatnumber) +  " with this pourch number " + str(pourchno) + " added Successfully "
                return render(request,"home.html",{'status1': aa} )


            
            elif int(pourchno) >= (401) and int(pourchno) <= (473) :

                a=overalldata.objects.create(fullname=fullname,phonenumber=phonenumber,flatnumber=flatnumber,parkingno="p4",pourchno=pourchno)
                a.save()
                aa = "data of flat " + str(flatnumber) +  " with this pourch number " + str(pourchno) + " added Successfully "
                return render(request,"home.html",{'status1': aa} )

            
            

        
    return render(request,"home.html")




def check_pourchnum(request):
    # print ("ok")
    if request.method =="GET":
        un = request.GET["user_n"]
        print ("here is un",un)
        if un == "no" or un=="NO":
            return HttpResponse ("Not Exists")
        else:

            check = overalldata.objects.filter(pourchno=un)
            print (len(check))
            
            if len(check) >= 1:
                return HttpResponse("Exists")
            else :
                return HttpResponse ("Not Exists")
            print (check,len(check))
            print (un)
    return HttpResponse("Hello")

def delete_product(request):
    context = {}
    if "pid" in request.GET:
        pid = request.GET["pid"]
        prd = get_object_or_404(overalldata,id=pid)
        context["product"]=prd
    if "action" in request.GET:
        prd.delete()

        data = str(prd.pourchno) + "from" + str (prd.parkingno) + "removed successfully"
        context["data"]=data
        

    return render(request,"delete_product.html",context)

def flats(request):
    flat = overalldata.objects.values_list('flatnumber',flat=True)
    flat =  list(flat)
    flat = '[%s]' % ', '.join(map(str, flat))
    final_list=[]
    avail=0
    reserve=0

    studio_flat = {109,116,209,216,309,316,409,416,509,516,609,616,709,716,809,811,906,916,
    1009,1016,1109,1116,1209,1216,1309,1316,1409,1416
    }
    
    
    for a in (studio_flat):
        print (a)
        if str(a) in flat:
            reserve = reserve + 1
            print ("ok")
        else:
            final_list.append(a)
            avail = avail + 1
            print ("not ok")
    
    final_list.sort()

    BKH3_FLAT={
        111,114,211,214,311,314,411,414,511,514,611,614,711,714,811,814,911,914,
    1011,1014,1111,1114,1211,1214,1311,1314,1411,1414    
    }
    final_list1=[]
    avail1=0
    reserve1=0
    for a in (BKH3_FLAT):
        print (a)
        if str(a) in flat:
            reserve1 = reserve1 + 1
            print ("ok")
        else:
            final_list1.append(a)
            avail1 = avail1 + 1
            print ("not ok")
    
    final_list1.sort()

    BKH1_FLAT = {
        104,105,106,107,117,118,119,120,121,
        204,205,206,207,217,218,219,220,221,
        304,305,306,307,317,318,319,320,321,
        404,405,406,407,417,418,419,420,421,
        504,505,506,507,517,518,519,520,521,
        604,605,606,607,617,618,619,620,621,
        704,705,706,707,717,718,719,720,721,
        804,805,806,807,817,818,819,820,821,
        904,905,906,907,917,918,919,920,921,
        1004,1005,1006,1007,1017,1018,1019,1020,1021,
        1104,1105,1106,1107,1117,1118,1119,1120,1121,
        1204,1205,1206,1207,1217,1218,1219,1220,1221,
        1304,1305,1306,1307,1317,1318,1319,1320,1321,
        1404,1405,1406,1407,1417,1418,1419,1420,1421,

    }

    final_list2=[]
    avail2=0
    reserve2=0
    for a in (BKH1_FLAT):
        print (a)
        if str(a) in flat:
            reserve2 = reserve2 + 1
            print ("ok")
        else:
            final_list2.append(a)
            avail2 = avail2 + 1
            print ("not ok")
    
    final_list2.sort()

    BKH2_FLAT = {
        101,102,103,108,110,112,113,115,122,123,124,
        201,202,203,208,210,212,213,215,222,223,224,
        301,302,303,308,310,312,313,315,322,323,324,
        401,402,403,408,410,412,413,415,422,423,424,
        501,502,503,508,510,512,513,515,522,523,524,
        601,602,603,608,610,612,613,615,622,623,624,
        701,702,703,708,710,712,713,715,722,723,724,
        801,802,803,808,810,812,813,815,822,823,824,
        901,902,903,908,910,912,913,915,922,923,924,
        1001,1002,1003,1008,1010,1012,1013,1015,1022,1023,1024,
        1101,1102,1103,1108,1110,1112,1113,1115,1122,1123,1124,
        1201,1202,1203,1208,1210,1212,1213,1215,1222,1223,1224,
        1301,1302,1303,1308,1310,1312,1313,1315,1322,1323,1324,
        1401,1402,1403,1408,1410,1412,1413,1415,1422,1423,1424,
    }
    
    final_list3=[]
    avail3=0
    reserve3=0
    for a in (BKH2_FLAT):
        print (a)
        if str(a) in flat:
            reserve3 = reserve3 + 1
            print ("ok")
        else:
            final_list3.append(a)
            avail3 = avail3 + 1
            print ("not ok")
    
    final_list3.sort()

    context ={
        'studioflats':final_list,
        'reserve':reserve,
        'avail':avail,
        'total':len(studio_flat),
        
        'studioflats1':final_list1,
        'reserve1':reserve1,
        'avail1':avail1,
        'total1':len(BKH3_FLAT),

        
        'studioflats2':final_list2,
        'reserve2':reserve2,
        'avail2':avail2,
        'total2':len(BKH1_FLAT),

        
        'studioflats3':final_list3,
        'reserve3':reserve3,
        'avail3':avail3,
        'total3':len(BKH2_FLAT),
    }

    return render(request,"remainingflats.html",context)

def delete_item(request):
    return render(request,"remainingflats.html")
    # return HttpResponse("done")

def slots(request):

    #in parking 1
    p1 = overalldata.objects.filter(parkingno='p1')
    print ("fuaksjksgsfkf",p1)
    reserved_p1 = p1.values_list('pourchno',flat=True)
    reserved_p1 =  list(reserved_p1)
    original = '[%s]' % ', '.join(map(str, reserved_p1))
    print("ori",original)
    total_reserved_p1 = parking1.objects.values_list('pourchno').count()

    print(type(reserved_p1))
    print(reserved_p1)
    print(total_reserved_p1)
    updates = []
    cont = 0
    available = 0 
    for avail in range(101,174):

        if str(avail) in original:
            print ("ok")
            cont = cont + 1 
            print(avail)
        else:
            updates.append(avail)

            available = available + 1
    print ("ip",updates)
    print ("reserved",cont)     
    print("available:",available)
    print (p1)

    p2 = overalldata.objects.filter(parkingno='p2')
    reserved_p2 = p2.values_list('pourchno',flat=True)
    reserved_p2 =  list(reserved_p2)
    original_p2 = '[%s]' % ', '.join(map(str, reserved_p2))
    print("ori",original)
    updates_p2 = []
    cont_p2 = 0
    available_p2 = 0 
    for avail in range(201,274):

        if str(avail) in original_p2:
            print ("ok")
            cont_p2 = cont_p2 + 1 
            print(avail)
        else:
            updates_p2.append(avail)

            available_p2 = available_p2 + 1
    print ("reserved",cont_p2)     
    print("available:",available_p2)


    p3 = overalldata.objects.filter(parkingno='p3')
    reserved_p3 = p3.values_list('pourchno',flat=True)
    reserved_p3=  list(reserved_p3)
    original_p3 = '[%s]' % ', '.join(map(str, reserved_p3))
    print("ori",original)
    updates_p3 = []
    cont_p3 = 0
    available_p3 = 0 
    for avail in range(301,374):

        if str(avail) in original_p3:
            print ("ok")
            cont_p3 = cont_p3 + 1 
            print(avail)
        else:
            updates_p3.append(avail)

            available_p3 = available_p3 + 1
    print ("reserved",cont_p3)     
    print("available:",available_p3)


    p4 = overalldata.objects.filter(parkingno='p4')

    reserved_p4 = p4.values_list('pourchno',flat=True)
    reserved_p4=  list(reserved_p4)
    original_p4 = '[%s]' % ', '.join(map(str, reserved_p4))
    print("ori",original)
    updates_p4 = []
    cont_p4 = 0
    available_p4 = 0 
    for avail in range(401,474):

        if str(avail) in original_p4:
            print ("ok")
            cont_p4 = cont_p4 + 1 
            print(avail)
        else:
            updates_p4.append(avail)

            available_p4 = available_p4 + 1
    print ("reserved",cont_p4)     
    print("available:",available_p4)

    overall = {
        'reserve':cont, 
        'reserve2':cont_p2, 
        'reserve3':cont_p3, 
        'reserve4':cont_p4,
        'avail': available, 
        'avail2': available_p2, 
        'avail3': available_p3, 
        'avail4': available_p4, 
    }


    return render(request,"remainingslots.html",{'context':updates,'context2':updates_p2,'context3':updates_p3,'context4':updates_p4,'overall':overall })


def all(request):
    context = {
    }
    overal = overalldata.objects.all()
    context["overal"]= overal
    print ("overall",overal)
    

    if "qury" in request.GET:
        q = request.GET["qury"]
        prd = overalldata.objects.filter(fullname__contains=q)
        context["overal"]= prd
        print ("qury",prd)
        return render(request,"all.html",{'context':prd})


    
    if "qury1" in request.GET:
        q = request.GET["qury1"]
        prd = overalldata.objects.filter(flatnumber__contains=q)
        context["overal"]= prd
        print ("qury1",prd)
        return render(request,"all.html",{'context':prd})



    
    if "qury2" in request.GET:
        q = request.GET["qury2"]
        prd = overalldata.objects.filter(pourchno__contains=q)
        context["overal"]= prd
        print ("qury2",prd)
        return render(request,"all.html",{'context':prd})

    return render(request,"all.html",{'context':overal})

    

        
def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect("/")