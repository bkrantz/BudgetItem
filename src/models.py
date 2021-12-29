from src.app import db

class BudgetItem(db.Model):
    __tablename__ = 'budget_items'

    item_id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    budget_id       = db.Column(db.Integer)
    display_name    = db.Column(db.String(255))
    value           = db.Column(db.DECIMAL(10, 2))
    parent_id       = db.Column(db.Integer, db.ForeignKey('budget_items.item_id'), nullable=True)
    created_on      = db.Column(db.TIMESTAMP, server_default=db.text("CURRENT_TIMESTAMP"))

    def to_json(self):
        return {
            "item_id":      self.item_id,
            "budget_id":    self.budget_id,
            "display_name": self.display_name,
            "value":        self.value,
            "parent_id":    self.parent_id,
            "created_on":   self.created_on
        }
