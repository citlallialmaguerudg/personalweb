# Página personal — Dra. Citlalli Almaguer Gómez

Sitio web académico personal (bilingüe ES/EN) de la Dra. Citlalli Almaguer Gómez,
Profesora–Investigadora en Fotónica, Óptica Visual y Divulgación Científica
(CUCEI, Universidad de Guadalajara).

## Estructura

| Archivo | Rol |
|---|---|
| `index.html` | Página principal. Carga `data.js` y `app.js`. |
| `data.js` | **Fuente única de todo el contenido** (bilingüe ES/EN). |
| `app.js` | Lógica de renderizado del sitio. |
| `styles.css` | Estilos / diseño. |
| `admin.html` | Panel de edición con login; publica cambios a GitHub. |
| `tools/build_cv.py` | Genera los 4 PDFs del CV (ES/EN, completo/sintético) desde `data.js`. |
| `tools/check_translations.py` | Verifica que `data.js` tenga ES y EN sin huecos. |
| `.github/workflows/build-cv.yml` | Acción que regenera los PDFs del CV cuando cambia `data.js`. |
| `assets/` | Foto de perfil, favicon y PDFs del CV (estos últimos se regeneran solos). |

## Cómo editar el contenido

Todo el contenido vive en `data.js`. El español es la fuente y el inglés su traducción.
Tras cualquier cambio, validar localmente:

```bash
node --check data.js
python3 tools/check_translations.py data.js   # debe reportar 0 faltantes
```

## Publicación

El sitio se sirve con **GitHub Pages** (rama `main`, carpeta raíz). Al hacer *push* de
`data.js`, la GitHub Action regenera automáticamente los PDFs del CV en `assets/`.
