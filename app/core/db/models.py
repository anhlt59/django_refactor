from django.db import models

from .fields import PositiveTinyIntegerField


class TimeStampMixin(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PolicyMixin(models.Model):
    """
    An abstract base class model that provides ``policy`` field
    to specify status is private or public
    """
    class POLICY(models.IntegerChoices):
        PRIVATE = 0
        PUBLIC = 1

    policy = PositiveTinyIntegerField(choices=POLICY.choices, default=POLICY.PRIVATE)

    class Meta:
        abstract = True


# queryset, manage & model for soft delete

class SoftDeleteQuerySet(models.query.QuerySet):
    """
    custom QuerySet
    Instead of removing instance sets ``is_deleted`` = 1 (True).
    """
    def delete(self):
        self.update(is_deleted=True)


class SoftDeleteManager(models.Manager):
    """
    custom models.Manager
    get only records with ``is_deleted`` = 0
    """
    _queryset_class = SoftDeleteQuerySet

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_deleted=False)


class SoftDeleteleModelMixin(models.Model):
    """
    An abstract base class model with a ``is_deleted`` field that
    marks entries that are deleted, but still kept in db.
    is_deleted = 1 mean deleted
    """
    is_deleted = PositiveTinyIntegerField(default=0)

    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)
