import os

def generate_invitations(template, attendees):
    # Verificar que el template es una cadena de texto
    if not isinstance(template, str):
        print("Error: El template no es una cadena de texto")
        return
    
    # Verificar que attendees es una lista de diccionarios
    if not isinstance(attendees, list) or not all (isinstance(item, dict) for item in attendees):
        print("Error: Los attendees no son una lista de diccionarios")
        return
    
    # Verificar si el template esta vacio
    if template.strip() == "":
        print("Error: El template esta vacio, no se generaron archivos de salida")
        return
    
    # Verificar si la lista de attendees esta vacia
    if len(attendees) == 0:
        print("No se proporconaron datos, no se generaron archivos de salida")
        return
    
    # Procesar cada attendees
    for index, attendee in enumerate(attendees, start=1):
        # Reemplazar los placeholders del template
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "Failed")
            invitation = invitation.replace(f"{{{{{key}}}}}", value if value else "Failed")


            # Nombre del archivo de salida
        output_filename = f"output_{index}.txt"
        
        # Escribir la invitación en un archivo
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)
        print(f"Archivo generado: {output_filename}")

# Código para probar la función
if __name__ == "__main__":
    # Leer el template de un archivo
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Lista de asistentes
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Llamar a la función con el template y la lista de attendees
    generate_invitations(template_content, attendees)
