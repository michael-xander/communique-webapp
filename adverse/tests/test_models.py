from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from patients.models import Patient
from adverse.models import EmergencyContact, AdverseEventType, AdverseEvent

