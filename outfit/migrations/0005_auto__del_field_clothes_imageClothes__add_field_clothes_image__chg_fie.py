# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Clothes.imageClothes'
        db.delete_column(u'outfit_clothes', 'imageClothes')

        # Adding field 'Clothes.image'
        db.add_column(u'outfit_clothes', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='Clothes.image', max_length=100),
                      keep_default=False)


        # Changing field 'Clothes.description'
        db.alter_column(u'outfit_clothes', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Clothes.name'
        db.alter_column(u'outfit_clothes', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Adding field 'Clothes.imageClothes'
        db.add_column(u'outfit_clothes', 'imageClothes',
                      self.gf('django.db.models.fields.files.ImageField')(default='Clothes.images', max_length=100),
                      keep_default=False)

        # Deleting field 'Clothes.image'
        db.delete_column(u'outfit_clothes', 'image')


        # Changing field 'Clothes.description'
        db.alter_column(u'outfit_clothes', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Clothes.name'
        db.alter_column(u'outfit_clothes', 'name', self.gf('django.db.models.fields.CharField')(max_length=150))

    models = {
        u'outfit.clothes': {
            'Meta': {'object_name': 'Clothes'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outfit.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'outfit.user': {
            'Meta': {'object_name': 'User'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['outfit']