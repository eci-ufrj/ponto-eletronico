# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'pessoal_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'pessoal', ['Person'])

        # Adding model 'Boss'
        db.create_table(u'pessoal_boss', (
            (u'person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pessoal.Person'], unique=True, primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.House'])),
        ))
        db.send_create_signal(u'pessoal', ['Boss'])

        # Adding model 'Worker'
        db.create_table(u'pessoal_worker', (
            (u'person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pessoal.Person'], unique=True, primary_key=True)),
            ('speciality', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pessoal', ['Worker'])

        # Adding M2M table for field workplaces on 'Worker'
        m2m_table_name = db.shorten_name(u'pessoal_worker_workplaces')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('worker', models.ForeignKey(orm[u'pessoal.worker'], null=False)),
            ('house', models.ForeignKey(orm[u'places.house'], null=False))
        ))
        db.create_unique(m2m_table_name, ['worker_id', 'house_id'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'pessoal_person')

        # Deleting model 'Boss'
        db.delete_table(u'pessoal_boss')

        # Deleting model 'Worker'
        db.delete_table(u'pessoal_worker')

        # Removing M2M table for field workplaces on 'Worker'
        db.delete_table(db.shorten_name(u'pessoal_worker_workplaces'))


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
        }
    }

    complete_apps = ['pessoal']