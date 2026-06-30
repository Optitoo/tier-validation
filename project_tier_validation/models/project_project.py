# Copyright 2026 Optitoo (Kolmio S. A.) (<http://www.optitoo.lu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = ["project.project", "tier.validation"]
    _state_from = ["to_define"]
    _state_to = ["on_track"]
    _tier_validation_manual_config = False

    def _get_requested_notification_subtype(self):
        return "project_tier_validation.project_tier_validation_requested"

    def _get_accepted_notification_subtype(self):
        return "project_tier_validation.project_tier_validation_accepted"

    def _get_rejected_notification_subtype(self):
        return "project_tier_validation.project_tier_validation_rejected"
