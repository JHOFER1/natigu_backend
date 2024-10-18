from app.extensions import db

class YourModel(db.Model):
    __tablename__ = 'your_table'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<YourModel {self.name}>'
