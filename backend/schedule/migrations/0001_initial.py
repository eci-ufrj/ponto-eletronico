# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeTable'
        db.create_table(u'schedule_timetable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('boss', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pessoal.Boss'])),
        ))
        db.send_create_signal(u'schedule', ['TimeTable'])

        # Adding model 'TimeTableLine'
        db.create_table(u'schedule_timetableline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.TimeTable'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pessoal.Worker'])),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['TimeTableLine'])


    def backwards(self, orm):
        # Deleting model 'TimeTable'
        db.delete_table(u'schedule_timetable')

        # Deleting model 'TimeTableLine'
        db.delete_table(u'schedule_timetableline')


    models = {
        u'pessoal.boss': {
            'Meta': {'object_name': 'Boss', '_ormbases': [u'pessoal.Person']},
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.House']"}),
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pessoal.Person']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'pessoal.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'pessoal.worker': {
            'Meta': {'object_name': 'Worker', '_ormbases': [u'pessoal.Person']},
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pessoal.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'workplaces': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.House']", 'symmetrical': 'False'})
        },
        u'places.house': {
            'Meta': {'object_name': 'House'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'gps_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'schedule.timetable': {
            'Meta': {'object_name': 'TimeTable'},
            'boss': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pessoal.Boss']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'schedule.timetableline': {
            'Meta': {'object_name': 'TimeTableLine'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.TimeTable']"}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pessoal.Worker']"})
        }
    }

    complete_apps = ['schedule']