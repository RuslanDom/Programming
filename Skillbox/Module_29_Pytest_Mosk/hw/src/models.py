from sqlalchemy import Column, String, Integer, ForeignKey, VARCHAR, Boolean, DateTime, UniqueConstraint
from .app import db




class Client(db.Model):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    surname = Column(VARCHAR(50), nullable=False)
    credit_card = Column(VARCHAR(50))
    car_number = Column(VARCHAR(10))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "credit_card": self.credit_card,
            "car_number": self.car_number
        }

# class Parking(db.Model):
#     __tablename__ = 'parking'
#     id = Column(Integer, primary_key=True, nullable=False)
#     address = Column(VARCHAR(100), nullable=False)
#     opened = Column(Boolean)
#     count_place = Column(Integer, nullable=False)
#     count_available_places = Column(Integer, nullable=False)
#
#
# class ClientParking(db.Model):
#     __tablename__ = 'client_parking'
#     id = Column(Integer, primary_key=True, nullable=False)
#     client_id = Column(Integer, ForeignKey('client.id'))
#     parking_id = Column(Integer, ForeignKey('parking.id'))
#     time_in = Column(DateTime)
#     time_out = Column(DateTime)
#
#     # Уникальное ограничение на пару (client_id, parking_id)
#     __table_args__ = (
#         UniqueConstraint('client_id', 'parking_id', name='unique_client_parking'),
#     )