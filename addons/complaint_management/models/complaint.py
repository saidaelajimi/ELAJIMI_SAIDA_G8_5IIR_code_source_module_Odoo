from odoo import models, fields

class ComplaintComplaint(models.Model):
    _name = "complaint.complaint"
    _description = "Complaint Management"

    name = fields.Char(string="Subject", required=True)
    description = fields.Text(string="Description")
    customer_name = fields.Char(string="Customer Name", required=True)
    category = fields.Selection([
        ("service", "Service"),
        ("product", "Product"),
        ("other", "Other"),
    ], string="Category", default="service")
    state = fields.Selection([
        ("draft", "Draft"),
        ("open", "Open"),
        ("resolved", "Resolved"),
    ], string="Status", default="draft")
    date_created = fields.Date(string="Date Created", default=fields.Date.today())
