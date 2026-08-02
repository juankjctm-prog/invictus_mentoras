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

## Pendiente: Diagnóstico de Cierre (antes/después real de competencias)

Objetivo: que RRHH pueda ver crecimiento real de las 11 competencias, no solo el punto de
partida. Hoy no hay ninguna remedición — hace falta construirla.

Plan propuesto:
1. Reutilizar `diagnostico_mentora.html` / `diagnostico_mentoreada.html` con un parámetro
   (ej. `?momento=cierre`) en vez de duplicar los formularios.
2. Guardar en la misma tabla `diagnostico_resultados`, agregando una columna `momento`
   (`'inicial' | 'cierre'`) para no romper lo que ya existe.
3. Disparar el diagnóstico de cierre automáticamente cuando `completed_days.length` llegue
   al total del programa (revisar cuál es el número real de días — el dashboard hoy asume
   45, pero la UI de la app dice "Día X de 78"; hay que confirmar cuál es correcto antes de
   construir esto) — un banner/notificación dentro de `app.html` invitando a completarlo.
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
- Discrepancia "45 días" (dashboard) vs "78 días" (texto en `app.html`) para la duración del
  programa — habría que confirmar el número real y unificarlo, especialmente antes de
  construir el diagnóstico de cierre (punto anterior), ya que ese trigger depende de saber
  cuál es el último día.
