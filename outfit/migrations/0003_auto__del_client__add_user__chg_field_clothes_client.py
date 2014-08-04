# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'outfit_client')

        # Adding model 'User'
        db.create_table(u'outfit_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('imageClient', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'outfit', ['User'])


        # Changing field 'Clothes.client'
        db.alter_column(u'outfit_clothes', 'client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['outfit.User']))

    def backwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'outfit_client', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('imageClient', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'outfit', ['Client'])

        # Deleting model 'User'
        db.delete_table(u'outfit_user')


        # Changing field 'Clothes.client'
        db.alter_column(u'outfit_clothes', 'client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['outfit.Client']))

    models = {
        u'outfit.clothes': {
            'Meta': {'object_name': 'Clothes'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outfit.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageClothes': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'outfit.user': {
            'Meta': {'object_name': 'User'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageClient': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['outfit']