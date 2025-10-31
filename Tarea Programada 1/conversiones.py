import json

def convertir_a_xml(nombre_base, filas, columnas):
    xml = [f"<{nombre_base}>", "<data>"]
    for fila in filas:
        xml.append("  <row>")
        for col in columnas:
            xml.append(f"    <{col}>{fila[col]}</{col}>")
        xml.append("  </row>")
    xml.append("</data>")
    xml.append(f"</{nombre_base}>")
    return "\n".join(xml)

def convertir_a_json(filas, columnas):
    data = [{col: fila[col] for col in columnas} for fila in filas]
    return json.dumps({"data": data}, indent=4, ensure_ascii=False)

def convertir_a_trama(filas, columnas):
    tramas = ["|".join(fila[col] for col in columnas) for fila in filas]
    return "\n".join(tramas)
