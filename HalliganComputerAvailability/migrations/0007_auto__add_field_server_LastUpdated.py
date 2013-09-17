# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Server.LastUpdated'
        db.add_column(u'HalliganComputerAvailability_server', 'LastUpdated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 9, 17, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Server.LastUpdated'
        db.delete_column(u'HalliganComputerAvailability_server', 'LastUpdated')


    models = {
        u'HalliganComputerAvailability.computer': {
            'ComputerNumber': ('django.db.models.fields.CharField', [], {'max_length': '7', 'primary_key': 'True'}),
            'LastUpdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Computer'},
            'RoomNumber': ('django.db.models.fields.IntegerField', [], {}),
            'Status': ('django.db.models.fields.CharField', [], {'default': "'AVAILABLE'", 'max_length': '9'})
        },
        u'HalliganComputerAvailability.computerinfo': {
            'ComputerNumber': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'ComputerStatus': ('django.db.models.fields.CharField', [], {'default': "'AVAILABLE'", 'max_length': '10'}),
            'Meta': {'object_name': 'ComputerInfo'},
            'RoomNumber': ('django.db.models.fields.IntegerField', [], {}),
            'Updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'HalliganComputerAvailability.lab': {
            'ClassName': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'DayOfWeek': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'EndDate': ('django.db.models.fields.DateField', [], {}),
            'EndTime': ('django.db.models.fields.TimeField', [], {}),
            'Meta': {'object_name': 'Lab'},
            'RoomNumber': ('django.db.models.fields.IntegerField', [], {}),
            'StartDate': ('django.db.models.fields.DateField', [], {}),
            'StartTime': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'HalliganComputerAvailability.server': {
            'ComputerName': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'LastUpdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Server'},
            'NumUsers': ('django.db.models.fields.IntegerField', [], {}),
            'Status': ('django.db.models.fields.CharField', [], {'default': "'ON'", 'max_length': '40'})
        },
        u'HalliganComputerAvailability.serverinfo': {
            'ComputerName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Meta': {'object_name': 'ServerInfo'},
            'NumUsers': ('django.db.models.fields.IntegerField', [], {}),
            'Updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['HalliganComputerAvailability']