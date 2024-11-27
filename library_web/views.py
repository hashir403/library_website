from django.shortcuts import render,redirect
from . models import Employee, Bookdetails
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
import os

# views.py
from django.shortcuts import render
from django.conf import settings
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def contact(request):
    success = False
    error = None

    if request.method == 'POST':
        # Extract user input from the form data
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')

        if user_email and user_message and username:
            # Your email credentials
            sender_email = "projecttest09python@gmail.com"  # Your email
            sender_password = "pzfb hxzl xgrh yvjp"  # Your Gmail App Password
            receiver_email = "projecttest09python@gmail.com"  # Your email to receive the message

            # Create a multipart message
            message = MIMEMultipart("alternative")
            message["Subject"] = f"Message from {username}"
            message["From"] = user_email
            message["To"] = receiver_email

            # Plain-text message body
            text = f"""\nHi,\nYou have received a message from {username} ({user_email}):\n\n{user_message}\n"""

            # Attach the plain-text message
            part1 = MIMEText(text, "plain")
            message.attach(part1)

            # Set up secure connection to Gmail's SMTP server
            context = ssl.create_default_context()

            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                success = True
            except Exception as e:
                error = str(e)
        else:
            error = "All fields are required."

    return render(request, 'contact.html', {'success': success, 'error': error})



bookname_from_db = ''
def download_file(request):
    if login_check == True:
        print(f"me login hon or mera login check  '{login_check}' ha or me file download kr rha hon\n\n")
        global bookname_from_db
        print('global bookname_from_db', bookname_from_db)
        import os

        # Your file path
        file_path = str(bookname_from_db)

        # Extract the file name
        file_name = os.path.basename(file_path)


        print('file_name',file_name)  # Output: Lahashil_Novel_CC9s5ak.pdf

        file_path = os.path.join('media', r"book_pdfs",file_name)
        print(file_path)
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    else:
        print(f"me login nhi hon or mera login check  '{login_check}' ha or me download function sy login page call krwa rha hon\n\n")
        return redirect('login')  
  



def search(request):
    if request.method == "POST":
        # Get the search input from the user
        given_name = request.POST['searchbar']
        # Use 'icontains' for case-insensitive search
        books = Bookdetails.objects.filter(bookName__icontains=given_name)
        
        # Render the search results in the 'search.html' template
        return render(request, 'search.html', {'books': books})
    
    # If it's a GET request, return to the home page or show an empty search page
    return render(request, 'search.html', {'books': []})


def home(request):
    data  = Bookdetails.objects.all()
    # data  = list(data)
    # content = {"data":data}
    print(data)
    li  = []
    for i in data:
        li.append(i)
    data = li
    return render(request, 'home.html',{'data':data})


def book_details(request,id):
    global bookname_from_db
    data = Bookdetails.objects.get(id = id)
    bookname_from_db = data.book
    print(' Insider bookname_from_db',bookname_from_db)
    return render(request, 'book-details.html',{"data":data})


def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')


login_check = False
def login(request):
    global login_check
    print(f"Login function call ho gya ha or mera login check '{login_check}' ha")
    if request.method == 'POST':
        print(f"inside login POST method or mera login check '{login_check}' ha")
        username = request.POST['username']
        password = request.POST['password']
        print(f"username: {username} | password: {password}")
        data = Employee.objects.filter(uname = username, upassword = password).exists()
        # HttpResponse("user is found")
        print(data)

        if data == True:
            login_check = True
            print(f"me login k andr hon or mera login check  '{login_check}' ha or me after login home page call krwa rha hon\n\n")
            return redirect('home')
        else:
            # return HttpResponse("User not found")
            print(f"me login hon or mera login check  {login_check} ha or mera user name find nhi huwa\n\n")
            return render(request, 'login.html', {'error_message': 'User not found'})
    print(f"Me login k POST method me nhi hon or mera login check  {login_check} ha\n\n")
    return render(request, 'login.html')

def signup(request):
    global login_check
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        data = Employee.objects.filter(uname = username, upassword = password).exists()
        print(data)

        if data == True:
            return render(request, 'signup.html', {'error_message': 'User already exists'})
        elif data == False:
            E_data = Employee.objects.create(uname = username, uemail = email, upassword = password)
            E_data.save()
            login_check = True
            return redirect('home')

    return render(request, 'signup.html')
