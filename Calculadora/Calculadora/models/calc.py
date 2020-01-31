from odoo import models, fields, api

class Calc(models.Model):
    _name = 'calc'

    numero_uno = fields.Float('Numero uno', required = True)
    numero_dos = fields.Float('Numero dos', required = True)

    suma = fields.Float(
        compute = "get_suma",
        String = "Suma",
        required = True
    )

    resta = fields.Float(
        compute = "get_resta",
        String = "Resta",
        required = True
    )

    multiplicacion = fields.Float(
        compute = "get_multiplicacion",
        String = "Multiplicacion",
        required = True
    )

    division = fields.Float(
        compute = "get_division",
        String = "Division",
        required = True
    )

    def get_suma(self):
        for record in self:
            record.suma = record.numero_uno + record.numero_dos

    def get_resta(self):
        for record in self:
            record.resta = record.numero_uno - record.numero_dos

    def get_multiplicacion(self):
        for record in self:
            record.multiplicacion = record.numero_uno * record.numero_dos

    def get_division(self):
        for record in self:
            if record.numero_dos == 0:
                record.division = 0
            else:
                record.division = record.numero_uno / record.numero_dos