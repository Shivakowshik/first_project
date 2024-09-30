from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request,'homepage.html')

def operation(request):
    n3 = ""
    try:
        if request.method == "POST":
            reset = request.POST.get('reset')

            if reset == 'reset':
                n3 = ""
            else:
                # Normal operation processing
                n1 = int(request.POST.get('num1'))
                n2 = int(request.POST.get('num2'))
                opr = request.POST.get('operation')

                if opr == "+":
                    n3 = n1 + n2
                elif opr == "-":
                    n3 = n1 - n2
                elif opr == "*":
                    n3 = n1 * n2
                elif opr == "/":
                    n3 = n1 / n2

    except:
        n3 = "invalid operation"
        print(n3)

    return render(request, 'homepage.html', {'result': n3})
