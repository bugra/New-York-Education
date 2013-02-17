# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Teacher.va_0506'
        db.add_column('app_teacher', 'va_0506',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Teacher.va_0607'
        db.add_column('app_teacher', 'va_0607',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Teacher.va_0708'
        db.add_column('app_teacher', 'va_0708',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Teacher.va_0809'
        db.add_column('app_teacher', 'va_0809',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Teacher.va_0506'
        db.delete_column('app_teacher', 'va_0506')

        # Deleting field 'Teacher.va_0607'
        db.delete_column('app_teacher', 'va_0607')

        # Deleting field 'Teacher.va_0708'
        db.delete_column('app_teacher', 'va_0708')

        # Deleting field 'Teacher.va_0809'
        db.delete_column('app_teacher', 'va_0809')


    models = {
        'app.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'app.school': {
            'Meta': {'object_name': 'School'},
            'additional_credit2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'environ_grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'environ_score': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'peer_index': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'percent2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'perf_category2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'perf_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prog_grade2010': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_grade2011': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'progress_report_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'readiness_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'readiness_score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'})
        },
        'app.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.School']", 'null': 'True'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'teacher_name_first_1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'teacher_name_last_1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'va_0506': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0607': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0708': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0809': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0910': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['app']