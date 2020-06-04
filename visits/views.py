from .models import Userip, VisitNumber, TotalCount
from django.utils import timezone
from django.conf import settings
from qqwry import QQwry


def ip2city(ip):
    q = QQwry()
    q.load_file(settings.QQWRY_ROOT)
    result = q.lookup(ip)
    if result is not None:
        city = result[0]
        type_net = result[1]
        return city + '\t' + type_net + '\n'
    else:
        return ''


# 修改网站访问量和访问ip等信息
def change_info(request):
    # 每一次访问，网站总访问次数加一
    count_nums = VisitNumber.objects.all()
    if count_nums:
        count_nums = count_nums[0]
        count_nums.total_count += 1
    else:
        count_nums = VisitNumber()
        count_nums.total_count = 1
    count_nums.save()

    # 记录访问ip和每个ip的次数
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
    # print(client_ip)

    ip_exist = Userip.objects.filter(ip=str(client_ip))
    if ip_exist:  # 判断是否存在该ip
        uobj = ip_exist[0]
        uobj.count += 1
        uobj.modified_time = timezone.now()
        if uobj.ip_country == '':
            uobj.ip_country = ip2city(str(client_ip))
    else:
        uobj = Userip()
        uobj.ip = client_ip
        uobj.count = 1
        uobj.modified_time = timezone.now()
        uobj.ip_country = ip2city(str(client_ip))
    uobj.save()

    # 增加今日访问次数
    date = timezone.now().date()
    print(timezone.now())
    today = VisitNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.day_count += 1
        temp.total_count = count_nums.total_count
    else:
        temp = VisitNumber()
        temp.date = date
        temp.day_count = 1
        temp.total_count = count_nums.total_count

    # temp.save()
    # today = VisitNumber.objects.filter(day="2020-6-2")
    # if today:
    #     temp = today[0]
    #     temp.day_count = 1
    #     temp.total_count = 28
    # temp.save()