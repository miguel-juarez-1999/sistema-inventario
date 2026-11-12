from producto import Producto


def buscar_producto(productos, nombre):
    """Devuelve los productos cuyo nombre contiene el texto buscado."""
    return [p for p in productos if nombre.lower() in p.nombre.lower()]


if __name__ == "__main__":
    inventario = [
        Producto("P001", "Teclado", 350.0, 20),
        Producto("P002", "Mouse", 180.0, 35),
        Producto("P003", "Teclado gamer", 890.0, 10),
    ]

    resultados = buscar_producto(inventario, "teclado")
    for p in resultados:
        p.mostrar()
        print("---")