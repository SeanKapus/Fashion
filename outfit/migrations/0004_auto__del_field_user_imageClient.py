# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.imageClient'
        db.delete_column(u'outfit_user', 'imageClient')


    def backwards(self, orm):
        # Adding field 'User.imageClient'
        db.add_column(u'outfit_user', 'imageClient',
                      self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100),
                      keep_default=False)


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['outfit']