# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'House'
        db.create_table(u'places_house', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('gps_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'places', ['House'])


    def backwards(self, orm):
        # Deleting model 'House'
        db.delete_table(u'places_house')


    models = {
        u'places.house': {
            'Meta': {'object_name': 'House'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'gps_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['places']