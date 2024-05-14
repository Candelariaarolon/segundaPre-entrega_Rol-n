from modulo1 import Prenda
from modulo2 import ClienteShop

def main():
    prendas = [
        Prenda("Remera", 2800),
        Prenda("Pantalon formal", 4500),
        Prenda("Jean roto", 3900),
        Prenda("Vestido de fiesta", 6000)
    ]

    cliente1 = ClienteShop("Cande", "Irigoyen, 3089", "candeerolonn@gmail.com")
    cliente1.registrarse()
    cliente1.iniciar_sesion()

    print(cliente1)

    cliente1.agregar_al_carrito(prendas[1])
    cliente1.agregar_al_carrito(prendas[3])

    cliente1.realizar_compra()
    cliente1.beneficio()
    cliente1.valoracion()

    print(f"Prendas favoritas de {cliente1.nombre}:")
    for prenda in cliente1.favoritos:
        print(f" - {prenda.nombre}")

if __name__ == "__main__":
    main()

