from django.shortcuts import render, redirect, HttpResponse
from App01 import models

# Create your views here.


def login(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    # with open("templates/login.html", "r", encoding="utf-8") as f:
    #     data = f.read()
    # return HttpResponse(data)
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        if email == "alex@oldboyedu.com" and pwd == "alexdsb":
            return redirect("http://www.luffycity.com")
        else:
            error_msg = "邮箱或密码错误，请重新输入！"
    return render(request, "login.html", {"error": error_msg})


def publisher_list(request):
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list.html", {"publisher_list": ret})


def add_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get("publisher_name", None)
        models.Publisher.objects.create(name=new_name)
        return redirect("/publisher_list/")
    return render(request, "add_publisher.html")


def del_publisher(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse("Delete row error!")


def edit_publisher(request):
    if request.method == "GET":
        edit_id = request.GET.get("id")
        if edit_id:
            edit_name = models.Publisher.objects.get(id=edit_id).name
            return render(request, "edit_publisher.html", {"publish_name": edit_name, "publish_id": edit_id})
        else:
            return HttpResponse("请求的编辑操作不存在！")
    edit_id = request.POST.get("publisher_id")
    edit_name = request.POST.get("publisher_name")
    edit_row = models.Publisher.objects.get(id=edit_id)
    edit_row.name = edit_name
    edit_row.save()
    return redirect("/publisher_list/")


def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"all_book": all_book})


def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_publisher_id = request.POST.get("publisher_id")
        models.Book.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect("/book_list/")
    publisher_list = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list": publisher_list})


def del_book(request):
    del_id = request.GET.get("id")
    models.Book.objects.get(id=del_id).delete()
    return redirect("/book_list/")


def edit_book(request):
    if request.method == "POST":
        new_title = request.POST.get("new_title", None)
        new_publisher_id = request.POST.get("new_publisher_id", None)
        old_id = request.POST.get("old_id", None)
        edit_obj = models.Book.objects.get(id=old_id)
        edit_obj.title = new_title
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect("/book_list/")
    edit_id = request.GET.get("id")
    edit_obj = models.Book.objects.get(id=edit_id)
    publisher_list = models.Publisher.objects.all()
    return render(request, "edit_book.html", {"old_id": edit_id, "book_obj": edit_obj, "publisher_list": publisher_list})


def author_list(request):
    ret = models.Author.objects.all()
    return render(request, "author_list.html", {"author_list": ret})
