# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MedicalObservationCode(models.Model):

    _name = "medical.observation.code"
    _description = "Medical Observation Code"

    name = fields.Char(required=True)
    color = fields.Char(string="Chart Color", default="#0000ff")

    integration_code = fields.Integer(required=True)
    default_observation_uom = fields.Many2one("medical.observation.uom")

    y_min = fields.Float(required=True)
    y_max = fields.Float(required=True)

    _sql_constraints = [
        ("name_uniq", "unique (name)", "Measure already exists!"),
        (
            "integration_code_uniq",
            "unique (integration_code)",
            "Measure already exists!",
        ),
    ]
