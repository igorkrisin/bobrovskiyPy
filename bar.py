#1

from math import *


class TicketsFactory:
    def making_tickets(self, type_ticket):
        ticket = self.get_ticket(type_ticket)
        return ticket

    def get_ticket(self, type_ticket):
        if type_ticket == 'RAIL':
            return self.create_rail_ticket
        elif format == 'FLIGHT':
            return self.create_rail_ticket
        else:
            raise ValueError(type_ticket)

    @staticmethod
    def create_rail_ticket(data_for_ticket):
        personal_data = {
            'name': data_for_ticket.name,
            'second_name': data_for_ticket.passang_second_name,
            'pass_serial_number': data_for_ticket.passp_serial_number,
            'wagon_number': data_for_ticket.wagon_number,
            'number_seat': data_for_ticket.pass_seat_number

        }
        return personal_data

    @staticmethod
    def create_flight_ticket(data_for_ticket):
        personal_data = {
            'name': data_for_ticket.name,
            'second_name': data_for_ticket.second_name,
            'pass_serial_number': data_for_ticket.serial_number,
            'flight_number': data_for_ticket.car_number,
            'number_seat': data_for_ticket.seat_number

        }
        return personal_data


class ShapeFactory:
    def print_shape(self, size_shape, type_shape):
        shape = self.get_shape(type_shape)
        return shape

    def get_shape(self, type_shape):
        if type_shape == 'SQUARE':
            return self.create_square
        elif type_shape == 'CIRCLE':
            return self.create_circle
        else:
            raise ValueError(type_shape)

    @staticmethod
    def creating_square(size_shape):
        area_square = size_shape*4

        return area_square

    @staticmethod
    def creating_circle(size_shape):
        area_circle = 3.14 * size_shape ^ 2

        return area_circle


class PointFactory:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    @staticmethod
    def creating_cartesian_point(x_coord, y_coord):
        return PointFactory(x_coord, y_coord)

    @staticmethod
    def creating_polar_point(rho, theta):
        return PointFactory(rho * cos(theta), rho * sin(theta))


#2 Никогда не использовал интерфейсы и абстрактные классы


