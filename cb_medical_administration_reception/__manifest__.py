# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Administration Location",
    "version": "12.0.1.0.0",
    "category": "Medical",
    "website": "https://github.com/tegin/cb-addons",
    "author": "Creu Blanca, Eficent",
    "license": "LGPL-3",
    "depends": ["cb_medical_administration_center"],
    "data": [
        "security/medical_security.xml",
        "data/ir_sequence_data.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False,
}
