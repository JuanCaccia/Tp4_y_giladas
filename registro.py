class Ticket:
    def __init__(self, codigo, patente, nacionalidad, tipo_vehiculo, forma_pago, pais_cabina, km_ult_cabina):
        self.codigo = codigo
        self.patente = patente
        self.nacionalidad = nacionalidad
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.km_ult_cabina = km_ult_cabina

    def __str__(self):
        return (f"ID Ticket: {self.codigo}"
                f" | Patente: {self.patente}"
                f" | Pais del Vehículo: {self.nacionalidad}"
                f" | Tipo Vehculo: {self.tipo_vehiculo}"
                f" | Forma Pago: {self.forma_pago}"
                f" | Pais Cabina {self.pais_cabina}"
                f" | Km desde ultima Cabina: {self.km_ult_cabina}")

    def argentino(self):
        if self.nacionalidad == "Argentina":
            print("\n Soy argentino me sobran los huevos\n")


'''
    def __str__(self):
        rta = 'ID ticket: ' + str(self.codigo)
        rta += ' || Patente: ' + str(self.patente)
        rta += ' || Pais del vehículo: ' + str(self.nacionalidad)
        rta += ' || Tipo vehículo: ' + str(self.tipo_vehiculo)
        rta += ' || Forma de pago: ' + str(self.forma_pago)
        rta += ' || País cabina: ' + str(self.pais_cabina)
        rta += ' || Km última cabina: ' + str(self.km_ult_cabina)
        return rta

'''
