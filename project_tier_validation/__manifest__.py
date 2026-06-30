# Copyright 2026 Optitoo (Kolmio S. A.) (<http://www.optitoo.lu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Project Tier Validation",
    "summary": "Extends Project to support a tier validation process.",
    "version": "19.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/OCA/tier-validation",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "project",
        "base_tier_validation",
    ],
    "data": [
        "data/mail_data.xml",
        "views/project_project.xml",
    ],
}
