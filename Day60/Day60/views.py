from django.shortcuts import HttpResponse, render


def login(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    # with open("templates/login.html", "r", encoding="utf-8") as f:
    #     data = f.read()
    # return HttpResponse(data)
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        if email == "alex@odlboyedu.com" and pwd == "alexdsb":
            return HttpResponse("Successfully!")
        else:
            return HttpResponse("False!")
