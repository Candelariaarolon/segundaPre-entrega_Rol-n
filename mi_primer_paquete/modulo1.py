class Prenda:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def ver_precios(prendas):
        for prenda in prendas:
            print(f"El precio de la {prenda.nombre} es de ${prenda.precio}")

    def inicializar_prendas():
        return [
            Prenda("Remera", 2800),
            Prenda("Pantalon formal", 4500),
            Prenda("Jean roto", 3900),
            Prenda("Vestido de fiesta", 6000)
        ]

prendas = Prenda.inicializar_prendas()

Prenda.ver_precios(prendas)
