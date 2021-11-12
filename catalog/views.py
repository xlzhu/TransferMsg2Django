from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Msg

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST" and request.POST:
        msg_username = request.POST.get("msg_username", None)
        msg_userphone = request.POST.get("msg_userphone", None)
        # msg_url = request.POST.get("msg_url", None) 修改需求：记录客户端完整 URL 路径，原 msg_url 失效
        msg_url = request.POST.get("url", None)
        msg_userage = request.POST.get("age", None)
        msg_userSIage = request.POST.get("sheb", None)
        msg_useredu = request.POST.get("school", None)
        msg_other = request.POST.get("msg_other", None)
        # 客户端原页面地址
        # client_url = msg_url
        
        msg = Msg()
        msg.msg_username = msg_username
        msg.msg_userphone = msg_userphone
        msg.msg_userage = msg_userage
        msg.msg_userSIage = msg_userSIage
        msg.msg_useredu = msg_useredu
        msg.msg_url = msg_url
        msg.msg_other = msg_userage + " " + msg_userSIage + " " + msg_useredu
        msg.save()
        return redirect(msg_url)
        #return HttpResponse("提交成功，稍后请注意接受信息或电话解答（内容较多时）")
        #return HttpResponse(url + ", " + msg_username + ", " + msg_userphone + ", " + msg_userage + ", " + msg_userSIage + ", " + msg_useredu)    
    return HttpResponse("your post has error")