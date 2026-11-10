
from pasajero import Pasajero


class MiCola:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    # 1. ENCOLAR PASAJERO

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La cola está llena")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1

        return True

    # 2. LISTAR PASAJEROS

    def listar(self):
        if self.cantidad == 0:
            print("  (cola vacía)")
            return

        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  <- FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  <- FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # 3. DESENCOLAR PASAJERO

    def desencolar(self):
        if self.esta_vacia():
            return None

        pasajero = self.datos[0]

        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return pasajero

    # 4. VER FRENTE

    def ver_frente(self):
        if self.esta_vacia():
            return None

        return self.datos[0]

    # 5. BUSCAR PASAJERO

    def buscar(self, numero):
        for i in range(self.cantidad):
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

        cantidad_inicial = self.cantidad

        for i in range(cantidad_inicial):
            pasajero = self.desencolar()

            if pasajero.numero != numero:
                self.encolar(pasajero)

        return True

    # 8. COPIAR COLA

    def copiar(self):
        nueva_cola = MiCola(self.capacidad)

        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])

        return nueva_cola

    # 9. LONGITUD

    def longitud(self):
        return self.cantidad

    # 10. VERIFICAR SI ESTÁ VACÍA

    def esta_vacia(self):
        return self.cantidad == 0
