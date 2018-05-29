import hashlib
import json
import logging
from collections import OrderedDict
from functools import partial

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.context_processors import csrf
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from edx_proctoring.services import ProctoringService
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey, UsageKey
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from requests.auth import HTTPBasicAuth
from xblock.core import XBlock
from xblock.django.request import django_to_webob_request, webob_to_django_response
from xblock.exceptions import NoSuchHandlerError, NoSuchViewError
from xblock.reference.plugins import FSService
from xblock.runtime import KvsFieldData

import static_replace
from capa.xqueue_interface import XQueueInterface
from courseware.access import get_user_role, has_access
from courseware.entrance_exams import user_can_skip_entrance_exam, user_has_passed_entrance_exam
from courseware.masquerade import (
    MasqueradingKeyValueStore,
    filter_displayed_blocks,
    is_masquerading_as_specific_student,
    setup_masquerade
)
from courseware.model_data import DjangoKeyValueStore, FieldDataCache
from edxmako.shortcuts import render_to_string
from eventtracking import tracker
from lms.djangoapps.grades.signals.signals import SCORE_PUBLISHED
from lms.djangoapps.lms_xblock.field_data import LmsFieldData
from lms.djangoapps.lms_xblock.models import XBlockAsidesConfig
from lms.djangoapps.lms_xblock.runtime import LmsModuleSystem
from lms.djangoapps.verify_student.services import VerificationService
from openedx.core.djangoapps.bookmarks.services import BookmarksService
from openedx.core.djangoapps.crawlers.models import CrawlersConfig
from openedx.core.djangoapps.credit.services import CreditService
from openedx.core.djangoapps.monitoring_utils import set_custom_metrics_for_course_key, set_monitoring_transaction_name
from openedx.core.djangoapps.util.user_utils import SystemUser
from openedx.core.lib.license import wrap_with_license
from openedx.core.lib.url_utils import quote_slashes, unquote_slashes
from openedx.core.lib.xblock_utils import request_token as xblock_request_token
from openedx.core.lib.xblock_utils import (
    add_staff_markup,
    replace_course_urls,
    replace_jump_to_id_urls,
    replace_static_urls,
    wrap_xblock
)
from student.models import anonymous_id_for_user, user_by_anonymous_id
from student.roles import CourseBetaTesterRole
from track import contexts
from util import milestones_helpers
from util.json_request import JsonResponse
from util.model_utils import slugify
from util.sandboxing import can_execute_unsafe_code, get_python_lib_zip
from xblock_django.user_service import DjangoXBlockUserService
from xmodule.contentstore.django import contentstore
from xmodule.error_module import ErrorDescriptor, NonStaffErrorDescriptor
from xmodule.exceptions import NotFoundError, ProcessingError
from xmodule.lti_module import LTIModule
from xmodule.modulestore.django import modulestore
from xmodule.modulestore.exceptions import ItemNotFoundError
from xmodule.x_module import XModuleDescriptor

