# -*- coding:utf-8 -*-

from .models import EmailVerifyRecord, Banner, UserProfile
import xadmin



class UserProfileAdmin(object):
    # list_display = ['nick_name', 'birday', 'gender', 'address', 'mobile', 'image']
    pass


xadmin.site.register(UserProfile, UserProfileAdmin)


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
