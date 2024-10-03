from books.models import Editorial, Autor, Libro
from datetime import date



editoriales=[
    Editorial(
        nombre='Editorial Aurora',
        direccion='Calle de los Pinos 123',
        ciudad='Ciudad del Sol',
        estado='Estado de las Estrellas',
        pais='País de la Luz',
        codigo_postal='12345',
        telefono='1234567890',
        email='contacto@editorialaurora.com',
        sitio_web='http://editorialaurora.com',
        fecha_fundacion=date(1995, 3, 15)
    )
]

editoriales = [
    {
        'nombre': 'Editorial Aurora',
        'direccion': 'Calle de los Pinos 123',
        'ciudad': 'Ciudad del Sol',
        'estado': 'Estado de las Estrellas',
        'pais': 'País de la Luz',
        'codigo_postal': '12345',
        'telefono': '1234567890',
        'email': 'contacto@editorialaurora.com',
        'sitio_web': 'http://editorialaurora.com',
        'fecha_fundacion': date(1995, 3, 15)
    },
    {
        'nombre': 'Editorial Horizonte',
        'direccion': 'Avenida del Cielo 456',
        'ciudad': 'Ciudad Celeste',
        'estado': 'Estado de los Ríos',
        'pais': 'País de las Nubes',
        'codigo_postal': '54321',
        'telefono': '0987654321',
        'email': 'info@editorialhorizonte.com',
        'sitio_web': 'http://editorialhorizonte.com',
        'fecha_fundacion': date(2001, 6, 20)
    },
    {
        'nombre': 'Ediciones del Viento',
        'direccion': 'Carrera del Viento 789',
        'ciudad': 'Villa del Aire',
        'estado': 'Estado de los Valles',
        'pais': 'País del Viento',
        'codigo_postal': '67890',
        'telefono': '1231231234',
        'email': 'ventas@edicionesviento.com',
        'sitio_web': 'http://edicionesviento.com',
        'fecha_fundacion': date(1987, 9, 30)
    },
    {
        'nombre': 'Editorial Centinela',
        'direccion': 'Paseo del Fuego 321',
        'ciudad': 'Ciudad del Guardián',
        'estado': 'Estado del Norte',
        'pais': 'País de los Centinelas',
        'codigo_postal': '98765',
        'telefono': '4321432143',
        'email': 'editor@editorialcentinela.com',
        'sitio_web': 'http://editorialcentinela.com',
        'fecha_fundacion': date(1998, 12, 5)
    },
    {
        'nombre': 'Editorial Mar Abierto',
        'direccion': 'Camino de la Costa 654',
        'ciudad': 'Ciudad Marina',
        'estado': 'Estado de las Olas',
        'pais': 'País del Mar',
        'codigo_postal': '24680',
        'telefono': '5556667778',
        'email': 'contacto@marabierto.com',
        'sitio_web': 'http://marabierto.com',
        'fecha_fundacion': date(2005, 2, 18)
    },
    {
        'nombre': 'Editorial Aurora',
        'direccion': 'Calle de los Pinos 123',
        'ciudad': 'Ciudad del Sol',
        'estado': 'Estado de las Estrellas',
        'pais': 'País de la Luz',
        'codigo_postal': '12345',
        'telefono': '1234567890',
        'email': 'contacto@editorialaurora.com',
        'sitio_web': 'http://editorialaurora.com',
        'fecha_fundacion': date(1995, 3, 15)
    },
    {
        'nombre': 'Editorial Horizonte',
        'direccion': 'Avenida del Cielo 456',
        'ciudad': 'Ciudad Celeste',
        'estado': 'Estado de los Ríos',
        'pais': 'País de las Nubes',
        'codigo_postal': '54321',
        'telefono': '0987654321',
        'email': 'info@editorialhorizonte.com',
        'sitio_web': 'http://editorialhorizonte.com',
        'fecha_fundacion': date(2001, 6, 20)
    },
    {
        'nombre': 'Editorial Centinela',
        'direccion': 'Paseo del Fuego 321',
        'ciudad': 'Ciudad del Guardián',
        'estado': 'Estado del Norte',
        'pais': 'País de los Centinelas',
        'codigo_postal': '98765',
        'telefono': '4321432143',
        'email': 'editor@editorialcentinela.com',
        'sitio_web': 'http://editorialcentinela.com',
        'fecha_fundacion': date(1998, 12, 5)
    },
    {
        'nombre': 'Ediciones del Viento',
        'direccion': 'Carrera del Viento 789',
        'ciudad': 'Villa del Aire',
        'estado': 'Estado de los Valles',
        'pais': 'País del Viento',
        'codigo_postal': '67890',
        'telefono': '1231231234',
        'email': 'ventas@edicionesviento.com',
        'sitio_web': 'http://edicionesviento.com',
        'fecha_fundacion': date(1987, 9, 30)
    },
    {
        'nombre': 'Editorial Mar Abierto',
        'direccion': 'Camino de la Costa 654',
        'ciudad': 'Ciudad Marina',
        'estado': 'Estado de las Olas',
        'pais': 'País del Mar',
        'codigo_postal': '24680',
        'telefono': '5556667778',
        'email': 'contacto@marabierto.com',
        'sitio_web': 'http://marabierto.com',
        'fecha_fundacion': date(2005, 2, 18)
    }
]



    
    
Editorial.objects.bulk_create(editoriales)

autores = [
    {'nombre': 'Gabriel', 'apellido': 'García Márquez', 'fecha_nacimiento': '1927-03-06', 'nacionalidad': 'Colombiana', 'biografia': 'Escritor, novelista y periodista, ganador del Premio Nobel de Literatura en 1982.', 'email': 'gabo@example.com', 'telefono': '123456789', 'sitio_web': 'https://gabrielgarciamarquez.com', 'premios': 'Premio Nobel de Literatura, Orden del Águila Azteca'},
    {'nombre': 'Isabel', 'apellido': 'Allende', 'fecha_nacimiento': '1942-08-02', 'nacionalidad': 'Chilena', 'biografia': 'Escritora y periodista chilena con una gran trayectoria literaria.', 'email': 'isabel.allende@example.com', 'telefono': '987654321', 'sitio_web': 'https://isabelallende.com', 'premios': 'Premio Nacional de Literatura de Chile'}
]
for autor in autores:
    Autor(
        autor['nombre'],
        autor['apellido'],
        autor['fecha_nacimiento'],
        autor['nacionalidad'],
        autor['biografia'],
        autor['email'],
        autor['telefono'],
        autor['sitio_web'],
        autor['premios']
        )
Autor.objects.bulk_create(autores)