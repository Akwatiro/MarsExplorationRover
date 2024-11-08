# Mars Exploration Rover

## Descripción
Este proyecto es una simulación de planificación de trayectorias para un rover en Marte utilizando STRIPS (Stanford Research Institute Problem Solver). El objetivo es que el rover se desplace desde un campamento base hasta el Monte Olimpo, cubriendo una distancia de 50 km y gestionando de forma óptima sus recursos, como el combustible y la capacidad de almacenamiento de bidones en sus bodegas.

## Estructura del Problema

### Situación Inicial
- **Ubicación**: El rover comienza en el campamento base (B) con el depósito de combustible vacío y ambas bodegas libres.
- **Recursos**: Hay bidones de combustible disponibles en el campamento base y en localizaciones intermedias.
- **Objetivo**: El objetivo es que el rover alcance el Monte Olimpo (M) con el depósito vacío, sin importar si tiene bidones en las bodegas.

### Componentes del Dominio
1. **Lugares**:
   - B: Campamento base.
   - L1, L2, L3, L4: Localizaciones intermedias donde el rover puede repostar.
   - M: Monte Olimpo, destino final.

2. **Bodegas del Rover**:
   - B1, B2: Las dos bodegas para almacenar bidones de combustible.

3. **Predicados**:
   - `roverEn(X)`: Indica la posición actual del rover.
   - `bodegaLibre(Bx)` / `bodegaOcupada(Bx)`: Estado de las bodegas del rover.
   - `bidonEn(X)`: Ubicación de bidones de combustible.
   - `depositoLleno` / `depositoVacio`: Estado del depósito de combustible.
   - `contiguo(X, Y)`: Indica si dos ubicaciones son adyacentes.

4. **Operadores**:
   - **desplazarse(X, Y)**: Mueve el rover de una ubicación a otra.
   - **repostarEn(X)**: Recarga el depósito de combustible.
   - **cargarBidonEn(X, Bx)**: Carga un bidón en la bodega.
   - **descargarBidonEn(X, Bx)**: Descarga un bidón de la bodega en una ubicación.

## Solución del Plan
El plan óptimo para alcanzar el Monte Olimpo incluye múltiples paradas para repostar y cargar o descargar bidones. A continuación, un resumen del plan:

1. `repostarEn(B)`
2. `desplazarse(B, L1)`
3. `repostarEn(L1)`
4. `cargarBidonEn(L1, B1)`
5. `desplazarse(L1, L2)`
6. `repostarEn(L2)`
7. `desplazarse(L2, L3)`
8. `descargarBidonEn(L3, B1)`
9. `repostarEn(L3)`
10. `desplazarse(L3, L4)`
11. `repostarEn(L4)`
12. `desplazarse(L4, M)`

Este plan asegura que el rover siempre tenga suficiente combustible para alcanzar la siguiente ubicación y, finalmente, el Monte Olimpo.

## Uso
Para ejecutar la planificación del rover en Python, utiliza el archivo [`roverMarte.py`](./roverMarte.py). Este archivo contiene el código que representa la situación inicial, las condiciones de contigüidad de las ubicaciones, y la definición de los operadores.

1. Clona el repositorio.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el archivo:
   ```bash
   python roverMarte.py

## Requisitos
- Python 3.x
- Librerías de soporte para lógica de planificación (si se requieren, instálalas usando `pip`).

## Contribuciones
Las contribuciones para mejorar la eficiencia de la planificación y el soporte para otros entornos son bienvenidas. Haz un fork del repositorio, implementa tus mejoras, y envía un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.
