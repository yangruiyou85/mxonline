import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


class CourseOrgAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


class TeacherAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
