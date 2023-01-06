import json
from json import JSONEncoder
from typing import List, Dict, Any
from dataclasses import dataclass


class ProductEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@dataclass
class Product:
    nombre: str
    codigo_barras: int
    fabricante: str
    categoria: str
    genero: str

    def __post_init__(self):
        self.nombre = self.nombre
        self.codigo_barras = self.codigo_barras
        self.fabricante = self.fabricante
        self.categoria = self.categoria
        self.genero = self.genero

    def __str__(self):
        return f"{self.nombre} - {self.codigo_barras} - {self.fabricante} - {self.categoria} - {self.genero}"


def get_products() -> List[Product]:
    return [
        Product("Zapatos XYZ", 8569741233658, "Deportes XYZ", "Zapatos", "Masculino"),
        Product("Zapatos ABC", 7452136985471, "Deportes XYZ", "Zapatos", "Femenino"),
        Product("Camisa DEF", 5236412896324, "Deportes XYZ", "Camisas", "Masculino"),
        Product("Bolso KLM", 5863219635478, "Carteras Hi-Fashion", "Bolsos", "Femenino"),
    ]


def group_products(products: List[Product]) -> Dict[str, Any]:
    result = {}
    for product in products:
        if product.fabricante not in result:
            result[product.fabricante] = {}
        if product.categoria not in result[product.fabricante]:
            result[product.fabricante][product.categoria] = {}
        if product.genero not in result[product.fabricante][product.categoria]:
            result[product.fabricante][product.categoria][product.genero] = []
        result[product.fabricante][product.categoria][product.genero].append(product)
    return result


def main():
    products = get_products()
    print(json.dumps(group_products(products), indent=4, cls=ProductEncoder))


if __name__ == "__main__":
    main()
