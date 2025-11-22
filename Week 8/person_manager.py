from Persona import Persona

personas = []

def store(data):
    nueva_persona = Persona(data[0], data[1], data[2], data[3], data[4])
    personas.append(nueva_persona)

def get_all_persons():
    return personas

def find_persons_by_name(name_sequence):
    result = []
    for persona in personas:
        if persona.nombre.find(name_sequence) != -1:
            result.append(persona)
    return result