import re

def slugify(texto):
    slug = (texto
        .lower()
        .strip()
        .replace(" ", "-")
    )
    slug = re.sub("[^\w\-]", "", slug)
    return slug

print(slugify("¡Hola, mundo! Esto es una cadena de ejemplo."))
print(slugify("¡Hola#,  %mundo!   456."))