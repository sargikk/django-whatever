# -*- coding: utf-8; mode: django -*-
from django.db import models
from django.test import TestCase
from unittest2.case import skipIf, expectedFailure
from django_any import any_model
from django_any.contrib import any_model_with_defaults

try:
    from mptt.models import MPTTModel, TreeForeignKey
except ImportError:
    TreeForeignKey = MPTTModel = None


if MPTTModel:
    class SimpleMPTTModel(MPTTModel):
        name = models.CharField(max_length=5)
        parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

        class Meta:
            app_label = 'django_any'

        class MPTTMeta:
            order_insertion_by = ['name']

    @any_model.register(SimpleMPTTModel)
    def any_redefined_model(model_cls, **kwargs):

        return any_model.default(model_cls, **kwargs)


@skipIf(MPTTModel is None, 'Run only if django-mptt is installed')
class TestModelWithMptt(TestCase):

    def test_any_model_with_defaults(self):
        node1 = any_model_with_defaults(SimpleMPTTModel, tree_id=1)
        node1.save()
        self.assertEqual(node1.lft, 1)
        self.assertEqual(node1.rght, 2)
        self.assertEqual(node1.level, 0)
        self.assertEqual(node1.tree_id, 1)

        node2 = any_model_with_defaults(SimpleMPTTModel, parent=node1, tree_id=1)
        node2.save()
        self.assertEqual(node2.lft, 2)
        self.assertEqual(node2.rght, 3)
        self.assertEqual(node2.level, 1)
        self.assertEqual(node2.tree_id, 1)

    def test_attributes_not_specified(self):
        node1 = any_model(SimpleMPTTModel, tree_id=1)
        node1.save()
        self.assertEqual(node1.lft, 1)
        self.assertEqual(node1.rght, 2)
        self.assertEqual(node1.level, 0)
        self.assertEqual(node1.tree_id, 1)

        node2 = any_model(SimpleMPTTModel, parent=node1, tree_id=1)
        node2.save()
        self.assertEqual(node2.lft, 2)
        self.assertEqual(node2.rght, 3)
        self.assertEqual(node2.level, 1)
        self.assertEqual(node2.tree_id, 1)