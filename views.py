from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from myapp.models import *

def login(request):
    return render(request,"login.html")

def login_post(request):
    username=request.POST['textfield']
    password = request.POST['textfield2']

    lobj=Login.objects.filter(username =username,password=password)
    if lobj.exists():
        lobj2=Login.objects.get(username = username,password = password)
        request.session['lid']=lobj2.id
        if lobj2.type=='Admin':
            return HttpResponse("<script>alert('Login Successfull');window.location='/myapp/HOME/'</script>")
        elif lobj2.type=='user':
            return HttpResponse("<script>alert('Login Successfull');window.location='/myapp/HomeU1/'</script>")

        else:
            return HttpResponse("<script>alert('invalid username & password');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse('''<script>alert('user not found');window.location="/myapp/login/"</script>''')



    return HttpResponse('''<script>alert('Successfuldef add_Acreateprfl(request):
    return render(request,"Admin/ACreate profile.html")
def add_Acreateprfl_POST(request):
    CompanyName = request.POST['textfield']
    OwnerName = request.POST['textfield2']
    Logo = request.FILES['filefield']
    Email = request.POST['textfield3']
    LicenceId = request.POST['textfield4']
    Place = request.POST['textfield5']
    District = request.POST['textfield6']
    State = request.POST['textfield7']
    Pincode = request.POST['textfield8']
    PhoneNumber = request.POST['textfield9']

    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, Logo)
    path = fs.url(date)

    obj = Adminprofile()
    obj.CompanyName = CompanyName
    obj.OwnerName = OwnerName
    obj.Logo = path
    obj.Email = Email
    obj.LicenceId = LicenceId
    obj.Place = Place
    obj.District = District
    obj.State = State
    obj.District = District
    obj.Pincode = Pincode
    obj.PhoneNumber = PhoneNumber
    obj.save()
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/add_Acreateprfl/"</script>''')


def admin_view_pofile(request):
    res=Adminprofile.objects.get(id=1)
    return render(request,"Admin/AView profile.html",{'data':res})

def add_editprfl(request):
    res = Adminprofile.objects.get(id=1)
    return render(request,"Admin/AEdit profile.html",{'data':res})

def add_editprfl_POST(request):
    CompanyName = request.POST['textfield']
    OwnerName = request.POST['textfield2']

    Email = request.POST['textfield3']
    LicenceId = request.POST['textfield4']
    Place = request.POST['textfield5']
    District = request.POST['textfield6']
    State = request.POST['textfield7']
    Pincode = request.POST['textfield8']
    PhoneNumber = request.POST['textfield9']
    if 'filefield' in request.FILES:
        Logo = request.FILES['filefield']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, Logo)
        path = fs.url(date)

        obj = Adminprofile.objects.get(id=1)
        obj.CompanyName = CompanyName
        obj.OwnerName = OwnerName
        obj.Logo = path
        obj.Email = Email
        obj.LicenceId = LicenceId
        obj.Place = Place
        obj.District = District
        obj.State = State
        obj.District = District
        obj.Pincode = Pincode
        obj.PhoneNumber = PhoneNumber
        obj.save()
    obj = Adminprofile.objects.get(id=1)
    obj.CompanyName = CompanyName
    obj.OwnerName = OwnerName
    obj.Email = Email
    obj.LicenceId = LicenceId
    obj.Place = Place
    obj.District = District
    obj.State = State
    obj.District = District
    obj.Pincode = Pincode
    obj.PhoneNumber = PhoneNumber
    obj.save()
l');window.location="/myapp/admin_view_pofile/"</script>''')









def add_gallery(request):
    return render(request,"Admin/A gallery.html")


def add_gallery_POST(request):
    Image = request.FILES['image']
    Description = request.POST['textarea']

    date = datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs = FileSystemStorage()
    fs.save(date,Image)
    path=fs.url(date)

    obj=Gallery()
    obj.Description=Description
    obj.Image=path
    obj.date=datetime.now()
    obj.save()

    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/add_gallery/"</script>''')

def admin_view_gallery(request):
    res=Gallery.objects.all()
    return render(request,"Admin/A view gallery .html",{"data":res})





def add_Aserviceform(request):
    return render(request,"Admin/Aserviceform.html")

def add_Aserviceform_POST(request):

    RoomType = request.POST['textfield']
    Image = request.FILES['image']
    Details = request.POST['textarea']
    Squarefeet = request.POST['textfield3']
    Price = request.POST['textfield4']

    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, Image)
    path = fs.url(date)

    obj=Service()
    obj.RoomType=RoomType
    obj.Image = path
    obj.Details=Details
    obj.Squarefeet=Squarefeet
    obj.Price=Price
    obj.save()
    return HttpResponse('''<script>alert('Added Successfull');window.location="/myapp/Aviewservices/"</script>''')


def Aviewservices(request):
    sv=Service.objects.all().order_by('-id')
    return render(request,"Admin/Aviewservices.html",{"data":sv})

def delete_service(request,id):
    Service.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/myapp/Aviewservices/"</script>''')

def edit_service(request,id):
    service = Service.objects.get(id=id)
    return render(request, "Admin/edit_service.html",{'service':service})

def edit_service_post(request):
    id = request.POST['id']
    RoomType = request.POST['textfield']
    Details = request.POST['textarea']
    Squarefeet = request.POST['textfield3']
    Price = request.POST['textfield4']

    service = Service.objects.get(id=id)

    if 'image' in request.FILES:
        Image = request.FILES['image']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, Image)
        path = fs.url(date)
        service.Image=path
        service.save()

    service.RoomType=RoomType
    service.Details=Details
    service.Squarefeet=Squarefeet
    service.Price=Price
    service.save()
    # return redirect('/myapp/Aviewservices')
    return HttpResponse('''<script>alert('ok');window.location='/myapp/Aviewservices/'</script>
            # <link rel="stylesheet" href="http://cdn.jsdelivr.net/npm/sweetalert2010">
            # <script src="https://cdn.jsdelivr.net/npm/sweetaleart2010"></script>
            # <stript>
            # document.addEventListener("DOMContentLoaded",function(){
            # Swal.fire9({
            # icon:'error',
            # tittle:'category already exists',
            # confirmButtonText:'OK',
            # reverseButtons:true
            # }).then((result)  -> {
            #    window.location - '/add_new_category';
            #    }
            #    });
            #    });
            #    </script>
            # 
    ''')


def Aviewservices_POST(request):
    RoomType= request.POST['textfield']
    Image = request.POST['image']
    Details= request.POST['textarea']
    Squarefeet = request.POST['textfield3']
    Price = request.POST['textfield4']


    obj = Service.objects.filter(Date__range=[fromdate, to])
    return render(request, "Admin/Aviewservices.html", {"data": obj})


def add_Aview_customer_rqust(request):
    rw=Usercustom.objects.all()
    return render(request,"Admin/Aview customer rqust.html",{"data":rw})

def add_Aview_customer_rqust_POST(request):
    fromdate= request.POST['textfield']
    to = request.POST['textfield2']

    obj=Usercustom.objects.filter(Date__range=[fromdate,to])
    return render(request, "Admin/Aview customer rqust.html",{"data":obj})

def add_Aview_review(request):
    rw=Review.objects.all()

    return render(request,"Admin/Aview review.html",{"data":rw})
def add_Aview_review_POST(request):
    fromdate= request.POST['textfield']
    to = request.POST['textfield2']

    obj=Review.objects.filter(Date__range=[fromdate,to])
    return render(request, "Admin/Aview review.html",{"data":obj})


def add_Aview_rqst_admin(request):
    res=Userequest.objects.all()
    return render(request,"Admin/Aview rqst admin.html",{"data":res})
def add_Aview_rqst_admin_POST(request):
    fromdate= request.POST['textfield']
    to = request.POST['textfield2']

    obj = Userequest.objects.filter(date__range=[fromdate, to])
    return render(request, "Admin/Aview rqst admin.html", {"data": obj})

def add_Aviewpayment(request):

    res=Usercunstompayment.objects.all()

    return render(request,"Admin/Aviewpayment.html",{'data':res})

def add_Aviewusers(request):
    sr=User.objects.all()
    return render(request,"Admin/AViewusers.html",{"data":sr})

def add_Aviewusers_post(request):
    search = request.POST['textfield']

    obj = User.objects.filter(UserName__icontains=search)

    return render(request, "Admin/Aviewusers.html",{"data": obj})

# def add_bill(request,id):
#     order = ORDER_MAIN.objects.get(id=id).id
#     print(order)
#     # Fetch the associated order items
#     order_items = ORDER_SUB.objects.filter(ORDERMAIN__id=order)
#     print(order_items)  # Check what items are being fetched
#
#     total = 0  # Initialize total outside the loop
#     import random
#     inno=random.randint(00000,99999)
#     context=""
#     for item in order_items:
#         print(item)
#         # Accumulate total for each item
#         total += item.Quantity * item.PRODUCT.Rate
#         context = {
#             'oid':item.ORDERMAIN.id,
#             'uname':item.ORDERMAIN.USER.User_name,
#             'contact':item.ORDERMAIN.USER.Phone,
#             'invoiceno':inno,
#             'date':item.ORDERMAIN.Date,
#             'Package_Name': item.PRODUCT.Product_name,
#             'Tax':item.Tax,
#             'Amount':item.ORDERMAIN.Amount,
#             'total': total,
#         }
#         print(item.PRODUCT.Product_name)  # Debug print of context
#     return render(request,"User/bill.html",{'data':context})

    # return render(request, "User/billmain.html", {'data': context})



def admin_changepass(request):
    return render(request,"User/User change pass.html")
def admin_changepass_POST(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield1']
    confirm_password = request.POST['textfield2']
    res=Login.objects.get(id=request.session['lid'])
    if res.password==current_password:
        if new_password==confirm_password:
            res.password=new_password
            res.save()
            return HttpResponse('''<script>alert('password changed successfully');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password');window.location="/myapp/admin_changepass/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert('invalid password');window.location="/myapp/admin_changepass/"</script>''')

def Admin_add_Sentamount(request,id):
        return render(request, "Admin/Sentamount.html",{'id':id})

def Admin_add_Sentamount_POST(request):
        Amount = request.POST['textfield']
        PriceDetails = request.POST['textarea']
        id = request.POST['id']
        obj=Usercustom.objects.filter(id=id).update(amount=Amount,status='approved',PriceDetails=PriceDetails)
        return HttpResponse(
            '''<script>alert('success');window.location="/myapp/add_Aview_customer_rqust/"</script>''')


def admin_accept(request,id):
    Usercustom.objects.filter(id=id).update(status="approved")
    return HttpResponse(
        '''<script>alert('approved');window.location="/myapp/add_Aview_customer_rqust/"</script>''')


def admin_reject(request,id):
    Usercustom.objects.filter(id=id).update(status="rejected")
    return HttpResponse(
        '''<script>alert('reject');window.location="/myapp/add_Aview_customer_rqust/"</script>''')


def admin_accept2(request,id):
    Userequest.objects.filter(id=id).update(status="approved")
    return HttpResponse(
        '''<script>alert('approved');window.location="/myapp/add_Aview_rqst_admin/"</script>''')


def admin_reject2(request,id):
    Userequest.objects.filter(id=id).update(status="rejected")
    return HttpResponse(
        '''<script>alert('reject');window.location="/myapp/add_Aview_rqst_admin/"</script>''')

def admin_DELgal(request,id):
    Gallery.objects.get(id=id).delete()
    return HttpResponse(
        '''<script>alert('Deleted Successfull');window.location="/myapp/admin_view_gallery/"</script>''')


def HOME(request):
    return render(request, "Admin/Adminindex.html")


##user



def user_add_Uview_custstatus(request):
    data=Usercustom.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"User/U view cust status.html",{"data":data})




def user_add_Uview_custstatus_POST(request):

    fromdate = request.POST['textfield']
    to = request.POST['textfield2']

    data = Usercustom.objects.filter(USER__LOGIN_id=request.session['lid'],Date__range=[fromdate, to])

    # data=Usercustom.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"User/U view cust status.html",{"data":data})


def user_add_Uview_gallery(request):
    data=Gallery.objects.all()
    return render(request,"User/U view gallery .html",{'data':data})
def user_add_Uview_gallery_POST(request):
    data=Gallery.objects.all()
    return render(request,"Admin/A view gallery .html",{'data':data})

def user_add_Uview_service(request):
    res=Service.objects.all()
    return render(request,"User/U view service.html",{'data':res})
def user_add_Uview_service_post(request):
    search=request.POST['textfield']
    re=Service.objects.filter(RoomType__icontains=search)
    return render(request, "User/U view service.html",{'data':re})

def user_add_Ucustrqst(request):
    return render(request,"User/Ucustomize rqst send.html")
def user_add_Ucustrqst_POST(request):
    id = request.POST['id']
    Description = request.POST['textarea']
    Refferencephoto = request.FILES['fileField']

    date = datetime.now().date().strftime('%Y%m%d-H%MS')+".jpg"
    fs = FileSystemStorage()
    fs.save(date,Refferencephoto)
    path = fs.url(date)

    obj=Usercustom()
    obj.SERVICE_id=id
    obj.Description=Description
    obj.Refferencephoto=path
    obj.Date=datetime.now()
    obj.status='Requested'
    obj.USER=User.objects.get(LOGIN=request.session["lid"])
    obj.save()
    return HttpResponse('''<script>alert('Success');window.location="/myapp/HomeU/"</script>''')

def user_add_Uprofilecreation(request):
    return render(request, "User/signupindex.html")

def user_add_Uprofilecreation_POST(request):
    UserName = request.POST['textfield2']
    Email = request.POST['textfield3']
    ProfilePhoto = request.FILES['fileField']
    Phone = request.POST['textfield4']
    Address = request.POST['textfield5']
    District = request.POST['textfield6']
    State = request.POST['textfield7']
    Pincode = request.POST['textfield8']
    password = request.POST['textfield9']

    if Login.objects.filter(username=Email).exists():
        return HttpResponse('''<script>alert('Already Exist');window.location="/myapp/user_add_Uprofilecreation/"</script>''')

    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, ProfilePhoto)
    path = fs.url(date)

    Lg=Login()
    Lg.username=Email
    Lg.password=password
    Lg.type='user'
    Lg.save()
    ug=User()
    ug.UserName=UserName
    ug.Email=Email
    ug.ProfilePhoto = path
    ug.Phone = Phone
    ug.Address = Address
    ug.District = District
    ug.State = State
    ug.Pincode = Pincode
    ug.LOGIN=Lg
    ug.save()

    return HttpResponse('''<script>alert('successfully created');window.location="/myapp/login/"</script>''')

def user_edit_Uprofilecreation(request):
    res=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"User/edit_user_profile.html",{'data':res})

def user_edit_Uprofilecreation_POST(request):
    UserName = request.POST['textfield2']
    Email = request.POST['textfield3']
    Phone = request.POST['textfield4']
    Address = request.POST['textfield5']
    District = request.POST['textfield6']
    State = request.POST['textfield7']
    Pincode = request.POST['textfield8']
    ug=User.objects.get(LOGIN=request.session['lid'])

    if 'fileField' in request.FILES:
        ProfilePhoto = request.FILES['fileField']

        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, ProfilePhoto)
        path = fs.url(date)
        ug.ProfilePhoto = path
        ug.save()

    ug.UserName=UserName
    ug.Email=Email
    ug.Phone = Phone
    ug.Address = Address
    ug.District = District
    ug.State = State
    ug.Pincode = Pincode
    ug.save()

    return HttpResponse('''<script>alert('changed successfully');window.location="/myapp/uviewprofl/"</script>''')


def uviewprofl(request):
    res=User.objects.get(LOGIN=request.session['lid'])
    return render(request,"User/Uprofile.html",{'data':res})

def user_add_Usend_rqst(request,id):
    a=Service.objects.get(id=id)
    return render(request,"User/Ucustomize rqst send.html",{'data':a})
def user_add_Usend_rqst_POST(request):
    id = request.POST['id']
    Description = request.POST['textarea']
    Date = request.POST['textfield2']
    a=Usercustom()
    a.SERVICE_id=id
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.Description=Description
    a.status='Requested'
    a.Date=Date
    a.save()
    return HttpResponse('''<script>alert('Requested');window.location="/myapp/user_add_Uview_service/"</script>''')



def user_add_normal_Usend_rqst(request,id):

    a=Userequest()
    a.SERVICE=Service.objects.get(id=id)
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.status='Requested'
    a.Date=datetime.now().strftime('%Y-%m-%d')
    a.save()
    return HttpResponse('''<script>alert('Requested');window.location="/myapp/user_add_Uview_service/"</script>''')




def user_add_Usendreview(request):
    return render(request,"User/Usendreview.html")
def user_add_Usendreview_POST(request):
    review = request.POST['textarea']

    obj=Review()
    obj.Review=review
    import datetime
    obj.Date=datetime.datetime.now().date()
    obj.USER=User.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert('Success');window.location="/myapp/HomeU/"</script>''')

def user_add_Sendpayment(request):
    return render(request,"User/USentpayment.html")
def user_add_Sendpayment_POST(request):
    Amount = request.POST['textfield']
    # PriceDetails = request.POST['textaria']
    return HttpResponse("ok")

def user_add_Uview_status(request):

    res=Userequest.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"User/Uview status.html",{"data":res})

def user_changepass(request):
    return render(request,"User/User change pass.html")

def user_changepass_POST(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield1']
    confirm_password = request.POST['textfield2']
    res = Login.objects.filter(id=request.session['lid'],password=current_password)
    if res.exists():
        Login.objects.get(id=request.session['lid'], password=current_password)
        if new_password == confirm_password:
            Login.objects.filter(id=request.session['lid']).update(password=confirm_password)
            return HttpResponse(
                '''<script>alert('password changed successfully');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert('password mismatched');window.location="/myapp/user_changepass/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert('invalid current password');window.location="/myapp/user_changepass/"</script>''')


def HomeU(request):
    return render(request,"User/Userindex.html")

def HomeU1(request):
    return render(request,"User/Userindex.html")


#####################

def raz_pay(request,amount,id):

    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amount= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }


    res=Usercustom.objects.filter(id=id).update(paystatus='paid')
    res1=Usercustom.objects.get(id=id)

    obj = Usercunstompayment()
    obj.Date = datetime.now().strftime('%Y-%m-%d')
    obj.Amount = amount
    obj.status = 'paid'
    obj.USERCUSTOMREQUEST_id = id
    obj.save()

    create_report(res1.SERVICE.RoomType, res1.Date, res1.Description, res1.amount)










    return render(request, 'user/pp.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id']})







    # Function to create the PDF
def create_report(roomtype,date,description,amount):

    filename="C:\\Users\\91790\\PycharmProjects\\Homeplanner\\media\\report.pdf"
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Draw background image
    # c.drawImage(r"C:\Users\91790\PycharmProjects\Homeplanner\media\20240828-172248.jpg", 0, 0, width,
    #             height)  # Adjust path and size as necessary

    # Set title
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(colors.black)
    c.drawCentredString(1 * inch, height - 1 * inch, "Bill")

    # Set subheading
    c.setFont("Helvetica-Bold", 18)
    c.drawString(1 * inch, height - 1.5 * inch, "Subheading")

    # Add some text
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 2 * inch, "Room Type :"+ roomtype)
    c.drawString(1 * inch, height - 2.5 * inch, "Date :" + str(date) )
    c.drawString(1 * inch, height - 3 * inch, "Description :" + description)
    c.drawString(1 * inch, height - 3.5 * inch, "Amount :" + str(amount))
    # c.drawString(1 * inch, height - 7.5 * inch, "You can add more content here.")

    # Save the PDF
    c.save()

# Call the function to create the report


def normal_raz_pay(request,amount,id):

    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amount= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }


    res=Userequest.objects.filter(id=id).update(paystatus='paid')
    res1=Userequest.objects.get(id=id)

    obj=Userservicepayment()
    obj.Date=datetime.now().strftime('%Y-%m-%d')
    obj.Amount=amount
    obj.status='paid'
    obj.REQUEST_id=id
    obj.save()
    create_report(res1.SERVICE.RoomType,res1.Date,res1.SERVICE.Details,amount)

    return render(request, 'user/pp.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id']})
def logout(request):
    try:
        del request.session['lid']
    except:
        pass
    return redirect('/myapp/login/')
