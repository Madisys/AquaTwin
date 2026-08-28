# AT-MORT-001 — Especificación técnica

## Misión
Anticipar incrementos anormales de mortalidad por jaula a 24 h, 72 h y 7 días, con incertidumbre, calidad de datos, explicabilidad y revisión humana.

## Unidad analítica
Jaula × tiempo, preservando site_id, cage_id y cohort_id.

## Targets
- excess_mortality_24h
- excess_mortality_72h (primario)
- excess_mortality_7d

La mortalidad esperada debe condicionarse por especie, etapa, peso, estacionalidad, centro, cohorte e historial. Los umbrales operacionales deberán calibrarse con datos reales.

## Features v1
### Ambiente
Temperatura, oxígeno disuelto/saturación, salinidad, pH, clorofila-a, corrientes y sus ventanas temporales.
### Producción
Biomasa, peso medio, edad de cohorte y densidad cuando esté disponible.
### Alimentación
Consumo, consumo/biomasa, índice de apetito y variaciones 24/72 h.
### Mortalidad
1 d, 3 d, 7 d, pendiente y anomalía respecto de baseline.
### Salud
Enfermedad activa, severidad, Caligus, días desde diagnóstico.
### Intervenciones
Tratamientos, manejo, transporte y desparasitación recientes.

## QA/QC
Cada registro debe incluir source_id, quality_flag, validation_status, ingestion_time y procedencia. Correcciones no eliminan el valor original.

## Modelos
1. Baseline epidemiológico/operacional.
2. Regresión logística.
3. Random Forest / gradient boosting si los datos lo justifican.
4. Modelos temporales sólo tras demostrar beneficio incremental.

## Métricas
AUROC, AUPRC, sensibilidad, especificidad, PPV, NPV, Brier Score, calibración y Early Warning Lead Time.

## Validación
- retrospectiva;
- shadow mode;
- prospectiva observacional;
- apoyo supervisado a decisión;
- evaluación de impacto.

Evitar particiones aleatorias que produzcan leakage entre jaulas, cohortes, centros o periodos relacionados. Incluir validación leave-site-out y temporal.

## Seguridad científica
Una predicción no es causalidad ni una indicación veterinaria. Las simulaciones contrafactuales se etiquetarán como escenarios del modelo. Toda acción sanitaria requiere decisión profesional.

## Fuentes externas
GSI se tratará como benchmark agregado; Sernapesca como referencia oficial chilena. No mezclar granularidades sin transformación y documentación explícitas.
