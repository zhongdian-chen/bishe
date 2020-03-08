from django.core import serializers
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import widgets
from django.shortcuts import render, HttpResponse
from movie import models
from django import forms
import re
import requests
from bs4 import BeautifulSoup


# Create your views here.

def main(request):
    return render(request, 'main.html')


def banner(request):
    return render(request, 'banner.html')


def layer(request):
    return render(request, 'layer.html')


class LogForm(forms.Form):
    loginphone = forms.CharField(
        max_length=11,
        error_messages={
            "required": "该字段不能为空"
        },
        widget=widgets.TextInput(attrs={'class': 'input'})
    )
    loginpwd = forms.CharField(
        error_messages={
            "required": "该字段不能为空"
        },
        widget=widgets.PasswordInput(attrs={'class': 'input'})
    )


def login(request):
    form_obj = LogForm()
    if request.method == "POST":
        form_obj = LogForm(request.POST)
        # 让form帮忙做校验
        if form_obj.is_valid():
            if models.UserRegisterInfo.objects.get(phone=form_obj.cleaned_data['loginphone']).phone == form_obj.cleaned_data['loginphone']:
                print('有这个人')
            else:
                print('没这个人')
            # print(ret.username + ret.userpwd)
            pass
        # return render(request, 'login.html', {'form_obj': form_obj})
    return render(request, 'login.html', {'form_obj': form_obj})


#
class RegForm(forms.Form):
    username = forms.CharField(
        max_length=8,
        label="用户名",
        error_messages={
            "required": "该字段不能为空"
        },
        validators=[
            # 中英文、数字、下划线
            RegexValidator(r'^[a-zA-Z0-9\u4e00-\u9fa5\_]+$', '用户名非法'),
        ],
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "input", "id": "name"})
    )
    userpwd = forms.CharField(
        label="密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "input", "id": "pwd"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "required": "该字段不能为空",
            "invalid": "密码非法",
        },
        validators=[
            # 必须有英文、数字，可包含特殊符号(~!@#$%^&*)
            RegexValidator(r'^(?=.*\d)(?=.*[a-zA-Z])[\da-zA-Z~!@#$%^&*]+$'),
        ]
    )
    re_pwd = forms.CharField(
        label="确认密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "input", "id": "re_pwd"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "required": "该字段不能为空",
        }
    )
    phone = forms.CharField(
        label="手机",
        max_length=11,
        # 自己定制校验规则
        # validators=[
        # RegexValidator(r'^[0-9]+$', '手机号必须是数字'),
        # RegexValidator(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$', '手机格式有误')
        # ],
        widget=widgets.TextInput(attrs={"class": "input", "id": "phone"}),
        # error_messages={
        #     "required": "该字段不能为空",
        # }
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if "金瓶梅" in username:
            raise ValidationError("不符合社会主义核心价值观")
        return username

    # 重写父类的clean方法
    def clean_re_pwd(self):
        # 此时通过校验的字段的数据都保存在 self.cleaned_data
        userpwd = self.cleaned_data.get("userpwd")
        re_pwd = self.cleaned_data.get("re_pwd")
        if userpwd != re_pwd:
            raise ValidationError("两次密码不一致")
        return re_pwd


def register(request):
    form_obj = RegForm()
    if request.method == "POST":
        form_obj = RegForm(request.POST)
        # 让form帮忙做校验
        if form_obj.is_valid():
            # 校验通过
            # 把数据存到数据库
            # 所有经过校验的数据都保存在 form_obj.cleaned_data
            del form_obj.cleaned_data["re_pwd"]
            print(form_obj.cleaned_data)

            models.UserRegisterInfo.objects.create(**form_obj.cleaned_data)
            flag = True
            # pass
            # return HttpResponse("ok")
        else:
            flag = False
        return render(request, 'register.html', {"form_obj": form_obj, "flag": flag})
        # return HttpResponse("no ok")
        # print(form_obj.changed_data)
        # del form_obj.changed_data["re_pwd"]
        # models.UserInfo.objects.create(**form_obj.changed_data)
    return render(request, 'register.html', {"form_obj": form_obj})


# def register(request):
#     ret = models.UserRegisterInfo.objects.all()
#     if request.method == 'POST':
#         phone = request.POST.get("phone", None)
#         username = request.POST.get("name", None)
#         userpwd = request.POST.get("pwd", None)
#         print(phone + username + userpwd)
#         return HttpResponse('ok')
#     return render(request, 'register.html', {"user_register_info": serializers.serialize('json', ret)})


def films(request):
    ret = models.FilmInfo.objects.get(id=1)
    return render(request, 'films.html', {"films_info": ret})


def tab_desc(request):
    return render(request, 'tab_desc.html')


def tab_celebrity(request):
    rets = models.CeleList.objects.filter(title='宠爱')
    type = models.CeleList.objects.filter(title='宠爱').values('type').distinct()
    return render(request, 'tab_celebrity.html', {"cele_list": rets, "cele_type": type})


def tab_img(request):
    ret = models.ImgList.objects.filter(title='宠爱')
    return render(request, 'tab_img.html', {"img_list": ret})


def buy_ticket(request):
    ret = models.FilmInfo.objects.get(id=1)
    return render(request, 'buy_ticket.html', {"films_info": ret})


def select_seat(request):
    return render(request, 'select_seat.html')


def pachong(request):
    type_list = []
    imgsrl = []
    picalt = []
    imgalt = []
    cele_list = []
    url = "https://maoyan.com/films/1279731"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__mta=51223958.1582186511387.1582188899635.1582189155701.23; uuid_n_v=v1; '
                  'uuid=1BB0108053B911EAABE96D628FDE9735CDB89454D42049DA9FA4986919BE3B02; '
                  '_lxsdk_cuid=17061aa38f3c8-09b722f06e5ed3-3f6b4d00-1fa400-17061aa38f3c8; '
                  '_lxsdk=1BB0108053B911EAABE96D628FDE9735CDB89454D42049DA9FA4986919BE3B02; '
                  'mojo-uuid=4b1d4d8e58019f75176fa0dd563437a8; mojo-session-id={'
                  '"id":"32c068737320fe3bcc1698dfa1ea65e8","time":1582186511447}; '
                  '_csrf=73f43f41003d6b13c483f9ee1ad0d95d9fba16c612e0e9d2d296e180aaf2fdad; mojo-trace-id=25; '
                  'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582188890,1582188894,1582188900,1582189156; '
                  'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582189156; _lxsdk_s=17061aa38f4-c16-9ad-66f%7C%7C46',
        'Host': 'maoyan.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('h1', class_='name').text.strip()
    div_tab = soup.find('div', class_='tab-celebrity')
    div_group = div_tab.find_all("div", class_="celebrity-group")

    # 获取演职人员类型、姓名、照片
    # 例如：导演,杨子,https://p0.meituan.net/moviemachine/0028d1c12af860aa00e261f87d265aae33124.jpg@128w_170h_1e_1c
    # for div_gr in div_group:
    #     div_type = div_gr.find("div", class_="celebrity-type").text.strip()
    #     types = re.match('.*', div_type, re.M | re.I)
    #     type_list.append(types.group())
    #     pic_list = div_gr.find_all("img", class_="default-img")
    #     for pic_li in pic_list:
    #         picurl = pic_li.attrs['data-src'].strip()
    #         picalt = pic_li.attrs['alt'].strip()
    #         imgsrl.append(picurl)
    #         imgalt.append(picalt)
    #         cele_list.append(types.group() + ',' + picalt + ',' + picurl)
    #
    # for i in cele_list:
    #     one_list = i.split(',')
    #     print('电影:' + title + '职位:' + one_list[0] + '姓名' + one_list[1] + '照片' + one_list[2])
    #     models.CeleList.objects.create(title=title, type=one_list[0], name=one_list[1], pic=one_list[2])

    div_tab_pic = soup.find('div', class_='tab-img')
    li_list = div_tab_pic.find_all("li")
    # print(li_list)
    for li in li_list:
        pic_li = li.find_all("img", class_="default-img")
        for i in pic_li:
            url = i.attrs['data-src'].strip()
            picalt.append(url)
    # print(picalt)

    for i in picalt:
        one_list = i.split(',')
        print('电影:' + title + '照片' + one_list[0])
        models.ImgList.objects.create(title=title, pic=one_list[0])

    return HttpResponse('ok')
