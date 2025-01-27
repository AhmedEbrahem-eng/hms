from odoo import models, fields, api


class PatientLogHistory(models.Model):
    _name = "hms.log.history"
    _description = "Patient Log History"
    _rec_name = "description"

    patient_id = fields.Many2one("hms.patient", string="Patient")
    description = fields.Text(string="Description")
