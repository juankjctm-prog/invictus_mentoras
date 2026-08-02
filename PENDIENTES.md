# Pendientes — Mujeres Mentoras

Registro de qué se arregló, qué falta y por qué, para no perder el hilo entre sesiones.
El detalle línea por línea de cada fix está en `git log` de este repo (`invictus_mentoras`).

## Resuelto (sesión 2026-08-02)

- **`current_day` retrocedía** al revisar un día ya completado, y podía duplicar filas en
  `mentoras_progress` por falta de `onConflict`. Ahora se persiste el día máximo alcanzado
  (`maxUnlockedDay`), monotónico. — `app.html`
- **Home mostraba "Día 1 / 0 PPM / 0%"** aunque hubiera progreso real en la nube, en
  cualquier navegador/dispositivo nuevo. Causa: `initUserSession` resolvía el día a mostrar
  con una clave 100% local (`mm_last_day_b1`) que nunca se sincroniza a Supabase, e ignoraba
  el día restaurado de la nube. También backfillea ahora las claves locales legacy
  (`mm_bN_dD_done/_ppm/_score`) que leen `renderKitMentoria`/`renderDashboard`. — `app.html`
- **Dashboard RRHH ("Avance del Ecosistema")**: si había filas duplicadas por usuario en
  `mentoras_progress`, se quedaba con la más vieja en vez de la más reciente. Corregido. Se
  agregaron columnas reales de **PPM** y **% Comprensión** (antes no existían en la tabla).
  — `dashboard_diagnostico.html`
- **Pestaña "Crecimiento de Mentoras"**: mostraba una comparación "Inicial vs Día 78"
  generada con `Math.random()` — no existe ningún segundo diagnóstico en el sistema, así que
  ese dato nunca fue real. Se reemplazó por dos secciones reales por pareja:
  - *Progreso Real Hoy*: día actual, mejor PPM, % comprensión promedio, última actividad
    (mismo cálculo que "Avance del Ecosistema", factorizado en `computeProgressStats()`).
  - *Diagnóstico Inicial*: las 11 competencias autoevaluadas al inicio
    (`resultados.brechasAuto` de la mentora, `resultados.brechas` de la mentada), que ya
    existían en Supabase pero el dashboard nunca las leía.
  — `dashboard_diagnostico.html`

## Resuelto (sesión 2026-08-02, parte 2 — reportado por Marjorie usando la plataforma)

- **Home mostraba "0 PPM / 0% Comprensión"** siempre, aunque Mi Kit sí mostraba el dato
  correcto. Causa: la pantalla real de Home usa los IDs `dash-ppm`/`dash-score`, y estos se
  llenaban con el resultado del **único día que se estuviera viendo** (`progresoLocal[dayIndex]`,
  vacío hasta terminar el quiz de ESE día), no con el mejor PPM / comprensión promedio que Mi
  Kit ya calculaba bien. Ahora `renderKitMentoria()` también escribe en `dash-ppm`/`dash-score`,
  y se eliminó la escritura vieja por-día. — `app.html`
- **Todos los días aparecían desbloqueados** desde el principio, sin importar el progreso
  real. `renderDashboard()` (el roadmap) no tenía ninguna lógica de bloqueo. Ahora bloquea
  (con 🔒 y sin click) cualquier día posterior a `maxUnlockedDay`, con una salvaguarda que
  también desbloquea un día más allá del día más alto ya completado, para no dejar a nadie
  con progreso previo atascada por este cambio. — `app.html`
- **Fases 5–11 mostraban el mismo contenido genérico todos los días.** Causa confirmada
  consultando Supabase directamente: `renderMentoraSession()` buscaba campos que no existen
  (`fase5_desc` ... `fase11_desc`); el contenido real y único por día SÍ está en
  `mentoras_content`, pero bajo otros nombres (`fase5_codificacion_dual`, `fase6_loci`,
  `fase7_analogia`, `fase8_ejercicio`, `fase10_metacognicion`, `fase11_ensayo` — verificado:
  string poblado en las 156 filas, 78 días × 2 roles). Corregidos los 6 nombres de campo.
  **Fase 9 (Feynman) queda pendiente de decisión** — ver abajo. — `app.html`
- Confirmado el número real de días del programa: **78** (156 filas en `mentoras_content` =
  78 días × 2 roles). Corregido `totalDays` en `dashboard_diagnostico.html` (era 45).

### Pendiente de decisión: Fase 9 (Técnica Feynman)

`fase9_feynman` en `mentoras_content` **no es texto**, es un booleano (`true` solo cuando
`día % 7 === 0`, ej. día 7, 14, 21...) — coincide exactamente con una variable ya calculada
en el código (`showFeynman`) que hoy no se usa en ningún lado. No hay ningún texto por-día
para esta fase en la base de datos, así que no se puede "arreglar" igual que las otras 6 —
sigue mostrando el texto genérico siempre. Falta decidir: ¿la Fase 9 debería verse distinta
(ej. un badge "Día de Repaso") solo esos días de repaso, o falta cargar contenido de texto
para ella igual que las demás? Sin esa definición no se puede tocar sin adivinar.

## Pendiente: Diagnóstico de Cierre (antes/después real de competencias)

Objetivo: que RRHH pueda ver crecimiento real de las 11 competencias, no solo el punto de
partida. Hoy no hay ninguna remedición — hace falta construirla.

Plan propuesto:
1. Reutilizar `diagnostico_mentora.html` / `diagnostico_mentoreada.html` con un parámetro
   (ej. `?momento=cierre`) en vez de duplicar los formularios.
2. Guardar en la misma tabla `diagnostico_resultados`, agregando una columna `momento`
   (`'inicial' | 'cierre'`) para no romper lo que ya existe.
3. Disparar el diagnóstico de cierre automáticamente cuando `completed_days.length` llegue a
   78 (confirmado — ver arriba).
4. Dashboard: la tabla de competencias en "Crecimiento de Mentoras" pasa de 2 columnas
   (solo inicial) a 4 (Mentora Inicial/Cierre, Mentada Inicial/Cierre).

## Otros hallazgos abiertos (detectados, no confirmados/arreglados)

- `vercel.json` reescribe `/` hacia `/Invictus_Mentoras.html`, un archivo que **no existe**
  en el repo. Si alguien entra por la raíz del sitio (en vez de `/app.html` directo), podría
  estar cayendo en un 404. No confirmado si esto afecta a usuarias reales — revisar cómo
  entran normalmente (¿link directo a `app.html`? ¿bookmarks?).
- En `dashboard_diagnostico.html`, el filtro que excluye PINs de prueba también excluye
  cualquier PIN real que termine en `"07"` (línea con `pin.endsWith('07')`). Si alguna
  mentora/mentada tiene un PIN así, desaparece de las tablas sin explicación.
- **Archivos duplicados con el mismo bug de Fases 5-11**: `Bloque1_Premium.html` ...
  `Bloque8_Premium.html` e `Invictus_Premium.html` tienen su propia copia de
  `renderMentoraSession()` con el mismo error de nombres de campo — NO se corrigieron en esta
  sesión (el fix se aplicó solo en `app.html`, que es el archivo que usan las usuarias reales
  según los datos de Supabase). `Master_Plan.html` sí enlaza a `Bloque2_Premium.html`, así que
  si esos archivos están desplegados y alguien los abre directamente, seguirán con el bug. Si
  se confirma que están en uso real, replicar el mismo fix ahí.
