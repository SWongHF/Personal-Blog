import os
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import User, Category, Post, Image, LastActivityRecord
from django.contrib.auth.decorators import login_required
import markdown2
import datetime
from django.core.files import File
from uuid import uuid4
# Create your views here.


def getPosts():
    posts = Post.objects.filter(hidden=False).order_by(
        "-priority", "-createdDate").all()
    return posts


def getPostsWithCategory(category_name):
    catObj = Category.objects.get(category_name=category_name)
    posts = Post.objects.filter(hidden=False).filter(
        category=catObj).order_by("-priority", "-createdDate").all()
    return posts


def category(request):
    tzinfo = datetime.timezone(datetime.timedelta(hours=+8.0))
    start_date = datetime.datetime(2023, 6, 26, 23, 27, tzinfo=tzinfo)
    end_date = datetime.datetime.now(tz=tzinfo)
    diff = abs((end_date-start_date).days)

    start_date = LastActivityRecord.objects.all()[0].last_activity
    t2 = abs((end_date-start_date).days)
    diff2 = str(t2)+" day(s) "
    if (t2 == 0):
        t2 = abs(((end_date-start_date).seconds)//3600)
        diff2 = str(t2)+" hr(s) "
    if (t2 == 0):
        t2 = abs(((end_date-start_date).seconds)//60) % 60
        diff2 = str(t2)+" min(s) "
    if (t2 == 0):
        t2 = abs((end_date-start_date).seconds)
        diff2 = str(t2)+" sec(s) "

    q = request.GET.get('q')
    posts = getPostsWithCategory(q)
    paginator = Paginator(posts, 10)
    posts_length = len(Post.objects.filter(hidden=False))
    if request.GET.get("page") != None:
        try:
            posts = paginator.page(request.GET.get("page"))
            page_range = list(paginator.get_elided_page_range(
                request.GET.get("page"), on_each_side=2, on_ends=1))
        except:
            posts = paginator.page(1)
            page_range = list(
                paginator.get_elided_page_range(1, on_each_side=2, on_ends=1))
    else:
        posts = paginator.page(1)
        page_range = list(paginator.get_elided_page_range(
            1, on_each_side=2, on_ends=1))
    return render(request, "blog/index.html", {"posts": posts, "tags": Category.objects.order_by('category_name').all(), "diff": diff, "lastactivity": diff2, "page_range": page_range, "posts_length": posts_length})


def index(request):
    tzinfo = datetime.timezone(datetime.timedelta(hours=+8.0))
    start_date = datetime.datetime(2023, 6, 26, 23, 27, tzinfo=tzinfo)
    end_date = datetime.datetime.now(tz=tzinfo)
    diff = abs((end_date-start_date).days)

    start_date = LastActivityRecord.objects.all()[0].last_activity
    t2 = abs((end_date-start_date).days)
    diff2 = str(t2)+" day(s) "
    if (t2 == 0):
        t2 = abs(((end_date-start_date).seconds)//3600)
        diff2 = str(t2)+" hr(s) "
    if (t2 == 0):
        t2 = abs(((end_date-start_date).seconds)//60) % 60
        diff2 = str(t2)+" min(s) "
    if (t2 == 0):
        t2 = abs((end_date-start_date).seconds)
        diff2 = str(t2)+" sec(s) "

    posts = getPosts()
    paginator = Paginator(posts, 10)
    posts_length = len(Post.objects.filter(hidden=False))
    if request.GET.get("page") != None:
        try:
            posts = paginator.page(request.GET.get("page"))
            page_range = list(paginator.get_elided_page_range(
                request.GET.get("page"), on_each_side=2, on_ends=1))
        except:
            posts = paginator.page(1)
            page_range = list(
                paginator.get_elided_page_range(1, on_each_side=2, on_ends=1))
    else:
        posts = paginator.page(1)
        page_range = list(paginator.get_elided_page_range(
            1, on_each_side=2, on_ends=1))
    return render(request, "blog/index.html", {"posts": posts, "tags": Category.objects.order_by('category_name').all(), "diff": diff, "lastactivity": diff2, "page_range": page_range, "posts_length": posts_length})


def denied(request):
    return render(request, "blog/denied.html")


def showImage(request, filename):
    try:
        image = Image.objects.get(filename=filename)
    except:
        return HttpResponse(status=400)
    return render(request, "blog/image.html", {"image": image})


def viewpost(request, post_suffix):
    tzinfo = datetime.timezone(datetime.timedelta(hours=+8.0))
    start_date = datetime.datetime(2023, 6, 26, 23, 27, tzinfo=tzinfo)
    end_date = datetime.datetime.now(tz=tzinfo)
    diff = abs((end_date-start_date).days)

    start_date = LastActivityRecord.objects.all()[0].last_activity
    t2 = abs((end_date-start_date).days)
    diff2 = str(t2)+" day(s) "
    if (t2 == 0):
        t2 = abs(((end_date-start_date).seconds)//3600)
        diff2 = str(t2)+" hr(s) "
    if (t2 == 0):
        t2 = abs(((end_date-start_date).seconds)//60) % 60
        diff2 = str(t2)+" min(s) "
    if (t2 == 0):
        t2 = abs((end_date-start_date).seconds)
        diff2 = str(t2)+" sec(s) "
    posts_length = len(Post.objects.filter(hidden=False))
    post = Post.objects.filter(hidden=False).get(suffix=post_suffix)
    post.views += 1
    # print(post.content)
    post.save()
    post.content = markdown2.markdown(post.content, extras=["fenced-code-blocks", "code-friendly", "spoiler", "tables", "task_list"])
    return render(request, "blog/post.html", {"post": post, "tags": Category.objects.order_by("category_name").all(), "diff": diff, "lastactivity": diff2, "posts_length": posts_length})


def manage(request):
    if request.user.has_perm('applications.admin_access'):
        tzinfo = datetime.timezone(datetime.timedelta(hours=+8.0))
        start_date = datetime.datetime(2023, 6, 26, 23, 27, tzinfo=tzinfo)
        end_date = datetime.datetime.now(tz=tzinfo)
        diff = abs((end_date-start_date).days)
        return render(request, "blog/manage.html", {"diff": diff, "posts_length": len(Post.objects.order_by("-priority", "-createdDate").all()), "tags_length": len(Category.objects.all()), "images_length": len(Image.objects.all())})
    else:
        # redirect to the other page
        return redirect("/denied", denied)


def post_manage(request):
    if request.user.has_perm('applications.admin_access'):
        return render(request, "blog/post_manage.html", {"posts": Post.objects.order_by("-priority", "-createdDate").all()})
    else:
        # redirect to the other page
        return redirect("/denied", denied)


def post_config(request):
    if request.user.has_perm('applications.admin_access'):
        if request.method == "DELETE":
            data = json.loads(request.body)
            suffix = data.get("content", "")
            if (Post.objects.filter(suffix=suffix).exists()):
                post = Post.objects.filter(suffix=suffix)
                post.delete()
                return JsonResponse({"message": "Success."}, status=200)
            else:
                return JsonResponse({"message": "Failed."}, status=400)
    else:
        return JsonResponse({"message": "Failed."}, status=400)


def post_edit(request):
    if request.user.has_perm('applications.admin_access'):
        q = request.GET.get('q')
        if (not Post.objects.filter(suffix=q).exists()):
            return redirect("/denied", denied)
        if request.method == "POST":
            title = request.POST.get("title", "")
            author = request.POST.get("author", "")
            suffix = request.POST.get("suffix", "")
            categories = request.POST.get("categories", "")
            priority = request.POST.get("priority", "")
            introduction = request.POST.get("introduction", "")
            content = request.POST.get("content", "")
            status = request.POST.get("status", "")
            if (q != suffix and Post.objects.filter(suffix=suffix).exists()):
                return JsonResponse({"message": "Failed."}, status=400)
            else:
                post = Post.objects.get(suffix=q)
                post.title = title
                post.author = author
                post.suffix = suffix
                post.category.clear()
                categories_t = categories.split(';')
                for ctg in categories_t:
                    ctg = ctg.strip()
                    if (Category.objects.filter(category_name=ctg).exists()):
                        post.category.add(
                            Category.objects.get(category_name=ctg))
                post.priority = priority
                post.introduction = introduction
                post.content = content
                if status == "0":
                    post.hidden = False
                else:
                    post.hidden = True
                post.save()
                return JsonResponse({"message": "Success."}, status=200)
        return render(request, "blog/post_manage_edit.html", {"post": Post.objects.get(suffix=q)})
    else:
        return JsonResponse({"message": "Failed."}, status=400)


def post_create(request):
    if request.user.has_perm('applications.admin_access'):
        q = request.GET.get('q')
        if request.method == "POST":
            title = request.POST.get("title", "")
            author = request.POST.get("author", "")
            suffix = request.POST.get("suffix", "")
            categories = request.POST.get("categories", "")
            priority = request.POST.get("priority", "")
            introduction = request.POST.get("introduction", "")
            content = request.POST.get("content", "")
            status = request.POST.get("status", "")
            post = Post()
            post.title = title
            post.author = author
            post.suffix = suffix
            categories_t = categories.split(';')
            for ctg in categories_t:
                ctg = ctg.strip()
                if (Category.objects.filter(category_name=ctg).exists()):
                    post.category.add(
                        Category.objects.get(category_name=ctg))
            post.priority = priority
            post.introduction = introduction
            post.content = content
            if status == "0":
                post.hidden = False
            else:
                post.hidden = True
            post.save()
            return JsonResponse({"message": "Success."}, status=200)
        return render(request, "blog/post_manage_create.html")
    else:
        return JsonResponse({"message": "Failed."}, status=400)


def category_manage(request):
    if request.user.has_perm('applications.admin_access'):
        return render(request, "blog/category_manage.html", {"tags": Category.objects.order_by("category_name").all()})
    else:
        # redirect to the other page
        return redirect("/denied", denied)


def category_config(request):
    if request.user.has_perm('applications.admin_access'):
        if request.method == "DELETE":
            data = json.loads(request.body)
            category_name = data.get("content", "")
            try:
                ctg = Category.objects.filter(category_name=category_name)
                ctg.delete()
                return JsonResponse({"message": "Success."}, status=200)
            except:
                return JsonResponse({"message": "Failed."}, status=400)
        if request.method == "POST":
            data = json.loads(request.body)
            category_name = data.get("content", "")
            if (not Category.objects.filter(category_name=category_name).exists()):
                ctg = Category(category_name=category_name)
                ctg.save()
                return JsonResponse({"message": "Success."}, status=200)
            else:
                return JsonResponse({"message": "Failed."}, status=400)
    else:
        return JsonResponse({"message": "Failed."}, status=400)


def image_manage(request):
    if request.user.has_perm('applications.admin_access'):
        images = Image.objects.order_by("-id")
        paginator = Paginator(images, 2)
        if request.GET.get("page") != None:
            try:
                images = paginator.page(request.GET.get("page"))
                page_range = list(paginator.get_elided_page_range(
                    request.GET.get("page"), on_each_side=2, on_ends=1))
            except:
                images = paginator.page(1)
                page_range = list(
                    paginator.get_elided_page_range(1, on_each_side=2, on_ends=1))
        else:
            images = paginator.page(1)
            page_range = list(paginator.get_elided_page_range(
                1, on_each_side=2, on_ends=1))
        return render(request, "blog/image_manage.html", {"images": images, "page_range": page_range})
    else:
        # redirect to the other page
        return redirect("/denied", denied)


def image_config(request):
    if request.user.has_perm('applications.admin_access'):
        if request.method == "DELETE":
            data = json.loads(request.body)
            filename = data.get("content", "")
            if (Image.objects.filter(filename=filename).exists()):
                ctg = Image.objects.get(filename=filename)
                if os.path.isfile(ctg.img.path):
                    os.remove(ctg.img.path)
                ctg.delete()
                return JsonResponse({"message": "Success."}, status=200)
            else:
                return JsonResponse({"message": "Failed."}, status=400)
        if request.method == "POST":
            filename = request.POST.get('filename')
            img = request.FILES.get('image')
            fn = filename
            while (Image.objects.filter(filename=fn).exists()):
                ud = '_'+uuid4().hex
                fn = '{}.{}'.format(
                    filename.split('.')[0]+ud[0:9], filename.split('.')[1])
            ctg = Image.objects.create(filename=fn, img=File(img))
            ctg.save()
            return JsonResponse({"message": "Success."}, status=200)

    else:
        return JsonResponse({"message": "Failed."}, status=400)
