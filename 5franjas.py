from PIL import Image

def seis_segmento_rgb(image_path):
    # Abre la imagen 
    original = Image.open(image_path).convert('RGB')
    width, height = original.size

    # Divide la imagen en seis partes iguales
    segments = [original.crop((0, i * height // 6, width, (i + 1) * height // 6)) for i in range(6)]

    # Convierte el segundo canal rojo, verde, azul, grises, blanco y negro,
    r, _, _ = segments[1].split()
    segments[1] = Image.merge("RGB", (r, Image.new("L", r.size), Image.new("L", r.size)))

    _, g, _ = segments[2].split()
    segments[2] = Image.merge("RGB", (Image.new("L", g.size), g, Image.new("L", g.size)))

    _, _, b = segments[3].split()
    segments[3] = Image.merge("RGB", (Image.new("L", b.size), Image.new("L", b.size), b))

    segments[4] = segments[4].convert('L').convert('RGB')

    segments[5] = segments[5].convert('1').convert('RGB')

    # Une los canales en una sola imagen
    new_image = Image.new('RGB', (width, height))
    for i, segment in enumerate(segments):
        new_image.paste(segment, (0, i * height // 6))

    # Rota la imagen 60 grados
    new_image = new_image.rotate(60, expand=True)
    new_image.save('imagen.png')
    new_image.show()

# cargando la imagen 
seis_segmento_rgb('lit.jpg')