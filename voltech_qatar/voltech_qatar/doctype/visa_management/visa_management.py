# -*- coding: utf-8 -*-
# Copyright (c) 2018, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import formatdate, getdate, cint, add_months, date_diff, add_days, flt, cstr, time_diff, time_diff_in_seconds, time_diff_in_hours,today
from datetime import date,datetime
import math
class VisaManagement(Document):
	pass

@frappe.whitelist()
def calculate_days():
	visamanage = frappe.db.sql("""select name from `tabVisa Management`""", as_dict=1)
	for visa in visamanage:
		# vm = frappe.db.get_value("Visa Management", visa["name"], "visa_expiry_date")
		visa = frappe.get_doc("Visa Management", visa["name"])
		expiry_date = visa.visa_expiry_date
		if visa.visa_type == 'Visit':
			if visa.visa_expiry_date:
				today = date.today()
				# today = date(2018,9,18)
				day = (expiry_date - today).days
				if day > 0:
					status = "Visa Expires on %d  days" % (day)
				else:
					status = "Visa Expired %d days ago" % (abs(day))
				visa.update({
					"status":status
				})
				visa.save(ignore_permissions=True)
				frappe.db.commit()
			