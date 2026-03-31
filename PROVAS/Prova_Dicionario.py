carros = {
    "vectra": {
        "marca": "chevrolet",
        "ano": "2010",
        "cor": "azul escuro"
}
}
print(carros["vectra"]["marca"])

carros["vectra"]["preco"] = int(24500)

print(carros.get("preco"))