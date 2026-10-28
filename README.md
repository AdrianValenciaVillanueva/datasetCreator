# viewTag — Buscador semántico de videos y Creador de Datasets

**viewTag** es un motor de búsqueda semántica de videos impulsado por **FastAPI**, **SigLIP** y **Qdrant**, ahora actualizado con capacidades completas para **previsualizar fotogramas** y **exportar datasets masivos etiquetados** para Machine Learning y visión por computador.

---

## 🚀 ¿Qué hay de nuevo en esta versión?

- **Caché y Previsualización de Fotogramas**: Los fotogramas extraídos se indexan y cachean eficientemente para ser servidos de inmediato como imágenes (`/frames/{video_name}/{frame_id}`).
- **Módulo de Creación de Datasets**: Nuevo servicio de aplicación para exportar muestras etiquetadas automáticamente a carpetas estructuradas acompañadas de un archivo `metadata.csv` maestro.
- **Soporte Completo Frontend (Vue.js)**: Interfaz web integrada para búsqueda visual, filtros de puntuación personalizables y exportación masiva con un solo clic.

---

## ¿Cómo funciona?

1. **Extrae fotogramas** del video (1 por segundo) con Decord.
2. **Convierte** cada fotograma y tu texto de búsqueda en vectores numéricos (embeddings) con SigLIP.
3. **Compara** el vector de tu búsqueda contra los vectores en Qdrant y te devuelve los fotogramas más parecidos.
4. **Visualiza y Exporta**: Explora las miniaturas en la interfaz web y organízalas en datasets etiquetados para entrenamiento.

---

## Estructura del Backend (`src/`)

```
src/
├── config/                  # Configuración centralizada (pydantic-settings)
├── domain/                  # Modelos de negocio e interfaces (vector repo, dataset repo)
├── application/             # Casos de uso (ProcessVideo, SearchVideo, DatasetService)
├── infrastructure/          # Implementaciones concretas (Decord, SigLIP, Qdrant, FileDataset)
├── observability/           # Logging estructurado (structlog) y Prometheus
└── api/                     # FastAPI (Rutas, DTOs y Rate Limiting)
```

---

## Instalación y Uso

### 1. Backend (Python)
```bash
cd video_searh_engine
python -m venv .venv
# En Windows:
.venv\Scripts\activate

pip install -e .
viewtag-api
```

### 2. Frontend (Vue.js)
```bash
cd C:\Users\4387472\Desktop\frontendViewTag
npm install
npm run dev
```
Accede a `http://localhost:5173` para usar la interfaz visual interactiva.

---

## Tests

```bash
cd video_searh_engine
python -m pytest tests -v
```
