# Gobernanza de datos AquaTwin

## Capas
1. OBSERVED: mediciones y registros originales.
2. DERIVED: transformaciones reproducibles.
3. PREDICTED: salidas de modelos versionados.
4. RECOMMENDED: escenarios o recomendaciones sometidas a revisión humana.

Nunca promover una predicción a dato observado ni una recomendación a resultado real.

## Datos sintéticos
Todo dataset sintético debe incluir `synthetic=true` y no puede emplearse para afirmar eficacia, seguridad, causalidad, desempeño biológico ni validación del modelo. Su uso se limita a pruebas de software, contratos, integración y CI.

## Procedencia
No sobrescribir silenciosamente valores originales. Las correcciones deben preservar original_value, corrected_value, motivo, autor y timestamp cuando corresponda.

## Modelos
Cada predicción conserva model_id, model_version, feature_version, input_hash y timestamp. Las predicciones históricas no se recalculan retroactivamente como si hubieran sido emitidas por una versión nueva.

## Supervisión
AT-MORT-001 es apoyo a decisión. Ninguna salida ejecuta automáticamente una intervención sanitaria o veterinaria.
