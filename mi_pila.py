
from pasajero import Pasajero


class MiPila:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    # 1. APILAR PASAJERO

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La pila está llena")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("Ya existe un pasajero con ese número")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # 2. LISTAR PASAJEROS

    def listar(self):
        if self.cantidad == 0:
            print("  (pila vacía)")
            return

        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  <- TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  <- FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # 3. DESAPILAR PASAJERO

    def desapilar(self):
        if self.esta_vacia():
            return None

        posicion = self.cantidad - 1
        pasajero = self.datos[posicion]

        self.datos[posicion] = None
        self.cantidad = self.cantidad - 1

        return pasajero

    # 4. VER TOPE

    def ver_tope(self):
        if self.esta_vacia():
            return None

        return self.datos[self.cantidad - 1]

    # 5. BUSCAR PASAJERO

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i

        return -1

    # 6. MODIFICAR PASAJERO

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento

        return True

    # 7. ELIMINAR POR NÚMERO

    def eliminar_por_numero(self, numero):
        if self.buscar(numero) == -1:
            return False

        auxiliar = MiPila(self.capacidad)

        while not self.esta_vacia():
            pasajero = self.desapilar()

            if pasajero.numero == numero:
                break

            auxiliar.apilar(pasajero)

        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())

        return True

    # 8. COPIAR PILA

    def copiar(self):
        nueva_pila = MiPila(self.capacidad)

        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])

        return nueva_pila

    # 9. LONGITUD

    def longitud(self):
        return self.cantidad

    # 10. VERIFICAR SI ESTÁ VACÍA

    def esta_vacia(self):
        return self.cantidad == 0
