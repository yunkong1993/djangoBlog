from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .get_index import get_index_list
from .get_detail import get_detail
from .models import VideoDetailItem
from .AES import decrypt_string
import json


class VideoView(TemplateView):
    # model = Post
    template_name = "video/video_index.html"
    context_object_name = "video"


class VideoDetailView(TemplateView):
    model = VideoDetailItem
    template_name = "video/video_detail.html"
    context_object_name = "video_detail"


def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    video_list = get_index_list(q=q)
    print(video_list)
    return render(request, 'video/video_index.html', {'video_list': video_list})


gb_video_items = []


def detail(request):
    m = request.GET.get('m')

    if not m:
        error_msg = "无效地址"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    video_detail, video_items = get_detail(url=m)
    # gb_video_items = video_items
    # print(video_detail)
    return render(request, 'video/video_detail.html', {'video_detail': video_detail, 'video_items': video_items})


def play(request):
    p = request.GET.get('p')

    if not p:
        error_msg = "无效地址"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')
    # pc = AesCrypto(key=b"keyskeyskeyskeyskeyskeyskeyskeys", IV=b"keyskeyskeyskeys")
    http = decrypt_string(p)
    http = json.loads(http)
    return render(request, 'video/video_play.html', {'http': http})
