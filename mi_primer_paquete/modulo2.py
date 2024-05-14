from modulo1 import Prenda 

class ClienteShop:
    def __init__(self, nombre, domicilio, email):
        self.nombre = nombre
        self.domicilio = domicilio
        self.email = email
        self.mediopago = None
        self.status = "Nuevo"
        self.favoritos = []
        self.carrito_compras = []
        self.compras = 0
        self.saldo = 0

    def registrarse(self):
        self.nombre = input("Ingrese su nombre: ")
        self.domicilio = input("Ingrese su domicilio: ")
        self.email = input("Ingrese su email: ")
        print(f"{self.nombre}, se registro exitosamente.")
    
    def iniciar_sesion(self):
        if self.nombre is not None:
            print(f"{self.nombre}, ha iniciado sesion.")
        else:
            print("El usuario no existe.")

    def agregar_a_favoritos(self, prenda):
        self.favoritos.append(prenda)
        print(f"{prenda.nombre} se agrego a tus favoritos.")

    def agregar_al_carrito(self, prenda):
        self.carrito_compras.append(prenda)
        print(f"{prenda.nombre} se agrego al carrito.")

    def remover_del_carrito(self, prenda):
        if prenda in self.carrito_compras:
            self.carrito_compras.remove(prenda)
            print(f"{prenda.nombre} ha sido eliminada del carrito.")
        else:
            print(f"{prenda.nombre} no se encuentra en el carrito.")

    def realizar_compra(self):
        if not self.carrito_compras:
            print("El carrito de compras esta vacio.")
            return

        print(f"Cliente: {self.nombre}")
        print(f"Domicilio: {self.domicilio}")
        print(f"Email: {self.email}")
        print("Productos en el carrito:")
        total = 0

        for prenda in self.carrito_compras:
            print(f" - {prenda.nombre}: ${prenda.precio}")
            total += prenda.precio

        print(f"Total de la compra: ${total}")

        self.mediopago = input("Seleccione su medio de pago: ")

        # Si pagas con VISA te hace un descuento y si pagas con MASTERCARD hace -$500
        if self.mediopago == "VISA":
            total -= total * 0.10  # Descuento del 10% para pagos con VISA
            print(f"Ha pagado ${total} con un descuento del 10%.")
        elif self.mediopago == "MASTERCARD":
            total -= 500  # Descuento de $500 para pagos con MASTERCARD
            print(f"Ha pagado ${total} con un descuento de $500.")
        else:
            print("El medio de pago no es valido.")

        self.compras += 1
        self.saldo += 200  # Te regala $200 cada vez que haces una compra para utilizar en otras compras en la app
    
    def consultarsaldo(self):
        return self.saldo

    def beneficio(self):
        if self.status == "Nuevo":
            print(f"{self.nombre} ha ganado un cupon de descuento para su proxima compra.")
    
    def valoracion(self):
        if self.compras > 15:
            print(f"{self.nombre} es un comprador ORO.")
        elif self.compras > 10:
            print(f"{self.nombre} es un comprador PLATA.")
        else:
            print(f"{self.nombre} ha realizado {self.compras} compras.")

    def __str__(self):
        return f"Cliente: {self.nombre}\nDomicilio: {self.domicilio}\nEmail: {self.email}"

cliente1 = ClienteShop("Cande", "Irigoyen, 3089", "candeerolonn@gmail.com")
cliente1.registrarse()
cliente1.iniciar_sesion()

print(cliente1)


cliente1.realizar_compra()
cliente1.beneficio()
cliente1.valoracion()

print(f"Prendas favoritas de {cliente1.nombre}:")
for prenda in cliente1.favoritos:
    print(f" - {prenda.nombre}")
