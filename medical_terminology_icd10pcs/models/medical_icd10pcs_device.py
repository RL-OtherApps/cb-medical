# Copyright 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MedicalIcd10pcsDevice(models.Model):

    _name = "medical.icd10pcs.device"
    _description = "Medical Icd10pcs Device"

    code = fields.Char(required=True)
    name = fields.Char(translate=True)
    section_id = fields.Many2one("medical.icd10pcs.section", required=True)
