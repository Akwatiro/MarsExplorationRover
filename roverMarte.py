import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg  # Para cargar la imagen de fondo

# Configuración de la posición de las localizaciones
locations = {
    'B': (1, 1),   # Campamento base
    'L1': (2, 2),  # Localización 1
    'L2': (3, 3),  # Localización 2
    'L3': (4, 2),  # Localización 3
    'L4': (5, 1),  # Localización 4
    'M': (6, 2)    # Monte Olimpo
}

# Pasos de la misión
steps = [
    ("Repostar en B (Base)", 'B', 'B'),
    ("Desplazarse de B a L1", 'B', 'L1'),
    ("Repostar en L1", 'L1', 'L1'),
    ("Cargar un bidón en L1", 'L1', 'L1'),
    ("Desplazarse de L1 a L2", 'L1', 'L2'),
    ("Repostar en L2", 'L2', 'L2'),
    ("Desplazarse de L2 a L3", 'L2', 'L3'),
    ("Descargar bidón en L3", 'L3', 'L3'),
    ("Repostar en L3", 'L3', 'L3'),
    ("Desplazarse de L3 a L4", 'L3', 'L4'),
    ("Repostar en L4", 'L4', 'L4'),
    ("Desplazarse de L4 a M (Monte Olimpo)", 'L4', 'M')
]

# Crear una nueva figura
fig, ax = plt.subplots(figsize=(10, 6))
plt.title("Mars Exploration Rover Mission")

# Cargar la imagen de fondo del mapa táctico
bg_image = mpimg.imread(r"C:\Users\alvrm\Desktop\Universidad\5. OPTATIVAS\Sistemas de Planificacion\Sistemas de Planificacion - Grupo 15\mapa_tactico.png")
ax.imshow(bg_image, extent=[0, 7, 0, 4], aspect='auto', alpha=0.5)  # Ajustar transparencia con alpha

# Dibujar las posiciones de las localizaciones
for loc, (x, y) in locations.items():
    color = 'green' if loc in ['B', 'L1', 'L2', 'L3', 'L4'] else 'red'
    ax.add_patch(patches.Circle((x, y), 0.2, color=color))
    plt.text(x, y + 0.3, loc, ha='center', color=color)  # Coloca el texto de las localizaciones más arriba

# Configurar límites y cuadrícula
plt.xlim(0, 7)
plt.ylim(0, 4)
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.grid(True)

# Índice de paso actual
current_step = 0
annotation = None
rover = None
completion_message = None
background_overlay = None

# Función para actualizar la misión en cada clic
def on_click(event):
    global current_step, annotation, rover, completion_message, background_overlay

    # Borrar la anotación, el rover y el mensaje anterior
    if annotation:
        annotation.remove()
    if rover:
        rover.remove()
    if completion_message:
        completion_message.remove()
    if background_overlay:
        background_overlay.remove()

    # Si hay más pasos, mostrar el siguiente
    if current_step < len(steps):
        description, start, end = steps[current_step]
        start_x, start_y = locations[start]
        end_x, end_y = locations[end]

        # Dibuja el rover en la posición final del paso
        rover = patches.Circle((end_x, end_y), 0.15, color='blue', label="Rover")
        ax.add_patch(rover)

        # Agrega la flecha que representa el movimiento
        if start != end:  # Solo dibujar flecha si se mueve
            ax.annotate(
                '', xy=(end_x, end_y), xytext=(start_x, start_y),
                arrowprops=dict(arrowstyle="->", color="blue", lw=1.5)
            )

        # Crear y mostrar la nueva anotación para el paso actual, desplazada hacia arriba
        annotation = ax.annotate(
            description, (end_x, end_y), 
            xytext=(0, 10), textcoords="offset points", ha='center', fontsize=8, color='black',
            arrowprops=dict(arrowstyle="->", color='gray', lw=0.5),
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3')  # Añadir fondo blanco
        )

        # Avanzar al siguiente paso
        current_step += 1

        # Refrescar la visualización
        plt.draw()
    else:
        print("Misión completada")
        
        # Crear un fondo difuminado para el mensaje de misión cumplida
        background_overlay = patches.Rectangle(
            (0, 0), 7, 4, linewidth=0, edgecolor='none', facecolor='black', alpha=0.5)
        ax.add_patch(background_overlay)

        # Mostrar el mensaje de misión cumplida en el centro
        completion_message = ax.text(
            3.5, 2, "Rover, Rover, misión cumplida!", ha='center', va='center', fontsize=20,
            color='white', weight='bold', alpha=1.0
        )

        # Refrescar la visualización
        plt.draw()

# Conectar el evento de clic a la función on_click
fig.canvas.mpl_connect('button_press_event', on_click)

# Mostrar la ventana gráfica
plt.show()
