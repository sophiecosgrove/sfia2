from application import db

class Fortunes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fortune = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return ''.join([
            'FortuneID: ', str(self.id), '\r\n',
            'Fortune: ', str(self.fortune), '\r\n'
        ])