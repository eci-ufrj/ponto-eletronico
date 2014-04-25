# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'db_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'db', ['User'])

        # Adding model 'Place'
        db.create_table(u'db_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='places', to=orm['db.User'])),
        ))
        db.send_create_signal(u'db', ['Place'])

        # Adding M2M table for field workers on 'Place'
        m2m_table_name = db.shorten_name(u'db_place_workers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'db.place'], null=False)),
            ('user', models.ForeignKey(orm[u'db.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'user_id'])

        # Adding model 'TimeCard'
        db.create_table(u'db_timecard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Place'])),
        ))
        db.send_create_signal(u'db', ['TimeCard'])

        # Adding model 'TimeCardEntry'
        db.create_table(u'db_timecardentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.User'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('timecard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.TimeCard'])),
        ))
        db.send_create_signal(u'db', ['TimeCardEntry'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'db_user')

        # Deleting model 'Place'
        db.delete_table(u'db_place')

        # Removing M2M table for field workers on 'Place'
        db.delete_table(db.shorten_name(u'db_place_workers'))

        # Deleting model 'TimeCard'
        db.delete_table(u'db_timecard')

        # Deleting model 'TimeCardEntry'
        db.delete_table(u'db_timecardentry')


    models = {
        u'db.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'places'", 'to': u"orm['db.User']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'workers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'workplaces'", 'symmetrical': 'False', 'to': u"orm['db.User']"})
        },
        u'db.timecard': {
            'Meta': {'object_name': 'TimeCard'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Place']"})
        },
        u'db.timecardentry': {
            'Meta': {'object_name': 'TimeCardEntry'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'timecard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.TimeCard']"}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.User']"})
        },
        u'db.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['db']