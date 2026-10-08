# AT-MORT-001 — Sprint 2

## Objetivo
Añadir Feature Store temporal y primitives de inferencia reproducible sin presentar el modelo como validado.

## Entregables
- features 24/72/168 h por jaula;
- hash reproducible del vector de entrada;
- salida predictiva versionada;
- limitaciones explícitas en toda inferencia;
- tests contra contaminación entre jaulas.

## Próximos gates
1. Persistencia PostgreSQL y migraciones.
2. Training pipeline con separación temporal y leave-site-out.
3. Calibración y evaluación de Early Warning Lead Time.
4. Registro/versionado de artefactos de modelo.
5. Endpoint /v1/predict sólo tras fijar un artefacto experimental reproducible.
6. Shadow mode con datos observacionales antes de cualquier uso operacional.

## Regla científica
Ningún resultado generado con datos sintéticos o modelos de prueba constituye evidencia de desempeño biológico, eficacia, seguridad o utilidad operacional.
