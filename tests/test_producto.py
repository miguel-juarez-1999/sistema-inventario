import io
import os
import sys
import unittest
from contextlib import redirect_stdout

# Permite importar el código de la carpeta src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from producto import Producto


def capturar_salida(producto):
    """Ejecuta mostrar() y devuelve el texto que imprime en pantalla."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        producto.mostrar()
    return buffer.getvalue()


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    def test_cp01_crear_producto(self):
        """CP01: el producto se crea con los datos proporcionados."""
        self.assertEqual(self.producto.codigo, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertEqual(self.producto.precio, 350)
        self.assertEqual(self.producto.existencia, 10)

    def test_cp02_mostrar_codigo(self):
        """CP02: se almacena y se muestra el código."""
        self.assertEqual(self.producto.codigo, "P001")
        self.assertIn("P001", capturar_salida(self.producto))

    def test_cp03_mostrar_nombre(self):
        """CP03: se conserva y se muestra el nombre."""
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertIn("Teclado", capturar_salida(self.producto))

    def test_cp04_mostrar_precio(self):
        """CP04: se almacena y se muestra el precio."""
        self.assertEqual(self.producto.precio, 350)
        self.assertIn("350", capturar_salida(self.producto))

    def test_cp05_mostrar_existencia(self):
        """CP05: se conserva y se muestra la existencia."""
        self.assertEqual(self.producto.existencia, 10)
        self.assertIn("10", capturar_salida(self.producto))

    def test_cp06_mostrar_informacion_completa(self):
        """CP06: mostrar() presenta los cuatro datos."""
        salida = capturar_salida(self.producto)
        for dato in ("P001", "Teclado", "350", "10"):
            self.assertIn(dato, salida)

    def test_cp07_crear_otro_producto(self):
        """CP07: un segundo producto no se confunde con el primero."""
        otro = Producto("P002", "Mouse", 180, 5)
        self.assertEqual(otro.codigo, "P002")
        self.assertEqual(otro.nombre, "Mouse")
        self.assertEqual(otro.precio, 180)
        self.assertEqual(otro.existencia, 5)
        self.assertEqual(self.producto.codigo, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")


if __name__ == "__main__":
    unittest.main()