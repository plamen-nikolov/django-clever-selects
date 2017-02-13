# coding: utf-8
"""
@author: Erik Telepovsky
@author: Steve Kossouho
"""
import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import EMPTY_VALUES as BASE_EMPTY_VALUES
from django.http import HttpResponse
from django.utils.cache import add_never_cache_headers
from django.views.generic.base import View


EMPTY_VALUES = BASE_EMPTY_VALUES + ('None',)


class ChainedSelectFormViewMixin(object):
    def get_form_kwargs(self):
        kwargs = super(ChainedSelectFormViewMixin, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ChainedSelectChoicesView(View):
    """ Ajax view for chained select field """

    child_set = None

    def dispatch(self, request, *args, **kwargs):
        """ Grab request values before dispatching HTTP method to view """
        self.field = request.GET.get("field")
        self.field_value = request.GET.get("field_value", None)
        self.parent_field = request.GET.get("parent_field")
        # Get the parent field value. It works for single and multiple selects.
        self.parent_value = request.GET.get("parent_value") or request.GET.getlist("parent_value[]")
        # If the 'parent_value' attribute is empty, do not return Nothing:
        # the client might want to artificially augment the 'parent_value'
        if self.parent_value in EMPTY_VALUES:
            pass
        return super(ChainedSelectChoicesView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """ Response for the 'GET' method """
        content_type = 'application/javascript'
        response = HttpResponse(json.dumps(self.get_choices(), cls=DjangoJSONEncoder), content_type=content_type)
        add_never_cache_headers(response)
        return response

    def empty_response(self):
        """ Return an empty response """
        content_type = 'application/javascript'
        response = HttpResponse(json.dumps((), cls=DjangoJSONEncoder), content_type=content_type)
        add_never_cache_headers(response)
        return response

    def get_child_set(self):
        return self.child_set

    def get_choices(self):
        """ Default method for populating select results """
        choices = []
        if self.parent_value in EMPTY_VALUES or self.get_child_set() is None:
            return []
        try:
            for obj in self.get_child_set().all():
                choices.append((obj.pk, str(obj)))
            return choices
        except ObjectDoesNotExist:
            return []
