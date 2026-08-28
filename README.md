# AquaTwin

Plataforma científico-productiva para apoyo a decisiones en salmonicultura mediante integración de datos, modelado predictivo, simulación y trazabilidad.

## AT-MORT-001 — Mortality Early Warning Engine

Primer MVP: anticipar incrementos anormales de mortalidad por jaula con horizontes de 24 h, 72 h y 7 días, cuantificando incertidumbre y explicando los factores que sustentan cada alerta.

### Principios

- Apoyo a decisión; nunca intervención veterinaria automática.
- Separación estricta entre datos observados, derivados, predicciones y recomendaciones.
- Procedencia y auditoría de datos y modelos.
- Comparación obligatoria de baseline frente a ML.
- Validación retrospectiva, shadow mode y validación prospectiva antes de uso operacional.
- Datos sintéticos exclusivamente para pruebas de software; nunca como evidencia biológica.

## Arquitectura inicial

`ingestión -> raw -> QA/QC -> normalización -> feature store -> baseline/ML -> calibración -> explicabilidad -> riesgo -> revisión humana -> outcome -> monitorización`

## Estado

Bootstrap técnico de AT-MORT-001 en desarrollo.
