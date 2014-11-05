__author__ = 'tyler'
from django.conf.urls import patterns, url

urlpatterns = patterns('HalliganComputerAvailability.views',
                       url(r'^room/(?P<RmNum>.+)/$',
                           'SpecificRoom',
                           name='SpecificRoom'),
                       url(r'^machine$',
                           'SpecificMachine',
                           name='SpecificMachine'),
                       url(r'^update/(?P<MchID>.+)/(?P<NewStatus>.+)',
                           'UpdateStatus',
                           name='UpdateStatus'),
                       url(r'^updateServer/(?P<MchID>.+)/(?P<NewStatus>.+)/(?P<num_users>\d+)',
                           'UpdateServer',
                           name='UpdateServer'),
                       url(r'^updateLab', 'UpdateLab', name='UpdateLab'),
                       url(r'^UpdateAllStatus',
                           'UpdateAllStatus',
                           name='UpdateAllStatus'),
                       )
