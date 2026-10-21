# Pendientes — Mujeres Mentoras

Registro de qué se arregló, qué falta y por qué, para no perder el hilo entre sesiones.
El detalle línea por línea de cada fix está en `git log` de este repo (`invictus_mentoras`).

## Auditoría general de contenido y progreso (sesión 2026-10-21)

Queja: lecturas que no salen, preguntas que no coinciden con los textos, inconsistencias
en usuarias. Diagnóstico hecho sobre un export completo de Supabase (solo lectura) y los
textos finales (bucket `textos` = mismos archivos que `\\JTPCAS\Users\Public\Downloads`).

### Resuelto

- **La BD se ignoraba en los días 1-30.** `initUserSession` buscaba `texto_lectura` /
  `preguntas` en el nivel superior de `content`, pero la BD los guarda en
  `content.fase2_lectura.{texto, comprension}` → siempre se mostraba
  `fallback_content_b2b.js`. Ahora se leen de `fase2_lectura`; el fallback solo cubre días
  sin contenido. — `app.html`
- **Contenido dañado** (en el fallback y en `src/data/json`): textos sin acentos o con letras
  separadas (archivos fuente en cp1252/UTF-16 leídos como UTF-8), "RESPUESTA MODELO" visible
  en las preguntas, opciones de relleno con la correcta siempre en 0, quizzes escritos para
  versiones viejas de las lecturas. Regenerado todo desde los textos finales con
  `scripts/build_contenido_mentoras.js` (detecta codificación, extrae lectura, parsea los
  quizzes oficiales) y verificado con `scripts/validar_contenido_mentoras.js`.
  - Días 6-10: el archivo oficial solo trae la clave → quizzes redactados desde la lectura
    (`src/data/contenido_mentoras/quizzes_dias6_10.json`). Día 10: la clave era de otro texto.
  - 67 preguntas (25 Mentora, 42 Mentada) que la lectura final no respaldaba, reemplazadas
    por otras basadas en la lectura, con cita de soporte
    (`src/data/contenido_mentoras/preguntas_reemplazo.json`).
  - Archivos finales equivocados reemplazados por la versión correcta de `\\JTPCAS`: Mentora
    d20 (era el checkpoint de Mentoreadas), Mentada d14 (era reescritura del d13), Mentada
    d28 (bloque de lectura vacío).
- **SQL sin filtro de rol**: los días 10-78 de Mentada en `mentoras_content` tenían el
  contenido de Mentora (lectura, título y casi todas las fases). Los días 1-30 se corrigen
  con `mentoras_content_dias1_30_{mentora,mentada}.sql` (siempre `WHERE role AND dia`).
- **Bajas y Lourdes**: el SQL del commit dd47cca nunca se aplicó (usaba `status`, columna
  inexistente). Nuevo `ecosistema_bajas_y_reinicio_lourdes.sql`: agrega `status`, da de baja
  a 022604/022605, Lourdes → Mentada de Marjorie desde cero. `app.html` bloquea el login de
  usuarias en `baja` y, con `answers.reset_epoch`, borra también el progreso local del
  navegador (si no, la lógica "local tiene más días que la nube" lo volvía a subir).
- Pestaña de la mentora "Mi mentada" se rompía: hacía `.trim()` sobre `answers`, que también
  guarda objetos. Quitados los emparejamientos Marjorie/Lourdes escritos a mano en el código.
- Las 12 filas "simuladas" de `mentoras_progress` (ver hallazgo de 2026-08-02) ya no existen:
  en el export de hoy no hay `updated_at` repetidos y todo el progreso es coherente.

### Pendiente

- **Días 31-78 no tienen contenido final** (confirmado por Juan). En la BD, Mentada 31-78
  tiene el contenido de Mentora: una mentoreada que llegue al día 31 verá contenido de
  mentora. La más avanzada (Eliana, mentora) va en el día 17.
- **Fases 1, 3 y 5-12 de Mentada (días 1-30)** siguen siendo las de Mentora en la BD. Fuente
  posible: `Playbook mentoreadas/` y `Complementos mentoreadas/` del Storage.
- **Audios**: no existen `Dia27Mentora.mp3` ni `Dia15Mentoreadas.mp3` (solo los .wav base);
  hay que renombrar en el bucket `audios`: `Dia18mentoreadas.mp3` → `Dia18Mentoreadas.mp3`,
  `Dia 23Mentoreadas.mp3` → `Dia23Mentoreadas.mp3`, `Dia27Mentereadas.mp3` →
  `Dia27Mentoreadas.mp3`.
- **Problemas de redacción en lecturas finales** (contenido del autor, no se tocó):
  Mentada d12 le habla a una mentora; Mentada d17 tiene errores en el resumen del bloque
  (omite el día 17, atribuye "Víctima" al d15 y Mehrabian al d16); Mentada d25 tiene "When
  tu mentora"; Mentoreadas 15 y 19 y las versiones de Mentora d20 / Mentada d14 vienen sin
  acentos en origen (el generador restaura solo los inequívocos: "estás"/"qué" pueden
  quedar sin tilde).
- Marjorie (012604): figuran días 1-11 completados pero solo hay puntajes de los días 4-10.
- Mabel, Stephany y Valentina tienen `current_day` igual a su último día completado (el
  quiz marca el día como completado antes de "Concluir día"). No las bloquea: el roadmap
  desbloquea el día siguiente al más alto completado.
- El `/dashboard` de la web Next.js lee `src/data/json/usuarias_b2b.json`, una foto fija del
  15-oct. Para ver avance real usar `dashboard_diagnostico.html` / `admin.html` (en vivo).

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

## Resuelto (sesión 2026-08-02, parte 3 — auditoría completa de las 16 mentoras/mentadas)

Se consultó Supabase directamente para las 16 usuarias reales (no solo Marjorie) por queja
generalizada de que el avance no se refleja en el dashboard RRHH ni el PPM/% Comprensión.

- **Causa raíz confirmada de "PPM/Comprensión siempre vacío" (100% de usuarias, 0/16 con
  datos)**: `evaluarQuizReal()` — la función real conectada al botón "Evaluar Comprensión"
  del flujo actual — calculaba el score pero nunca lo escribía en `progresoLocal[dayId]`,
  que es lo único que `saveProgress()` empaqueta en `answers` hacia Supabase y lo único que
  `computeProgressStats()` lee para Comprensión (PPM tiene un fallback a `ppm_history`, pero
  Comprensión no tiene ninguno). Existía una función vieja (`evaluarRecall()`, pantalla de
  lectura de un solo día con IDs `#reader-content`/`#comprension-block`) que sí lo hacía
  correctamente, pero ya no está conectada a ningún botón del flujo multi-día actual — quedó
  como código muerto. Corregido: `evaluarQuizReal()` ahora escribe `progresoLocal[dayId].ppm`
  y `.comprension`, llama a `saveProgresoLocal()`, y siempre sincroniza a la nube (antes solo
  sincronizaba la primera vez que se completaba el día — un quiz repetido con score distinto
  nunca se resincronizaba). — `app.html`

### Hallazgo abierto, no tocado: contaminación de datos en `mentoras_progress`

12 de las 16 filas de `mentoras_progress` comparten un `updated_at` **idéntico al
microsegundo** (`2026-07-31T22:48:09.330413Z`), con `current_day`/`completed_days`
sospechosamente uniformes (`2`/`[1]` en casi todos los casos). Ningún usuario real generaría
ese patrón. Coincide con el historial de commits de esta misma sesión de hoy
("forcing simulated dashboard data" → "reverting dashboard to real data"): parece que un
script de simulación escribió datos falsos directo a Supabase para que el dashboard se viera
poblado, y el "revert" posterior solo limpió marcadores falsos en `localStorage`
(`mm_b1_d1_ppm === '280'`, ver `initUserSession`) — nunca tocó las filas ya sembradas en la
nube. Es decir, el `Día 2` que hoy muestra el dashboard para la mayoría de mentoras/mentadas
probablemente **no es su progreso real**. No se modificó ninguna fila de producción sin
confirmar con el equipo — requiere decidir si se resetean esas 12 filas a `current_day: 1,
completed_days: []` para que puedan reconstruir su avance real (que ahora sí sincronizará
correctamente con el fix de arriba), o si se dejan y se corrigen solas conforme avancen.

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
