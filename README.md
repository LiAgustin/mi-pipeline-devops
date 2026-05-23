#Lizbeth San Agustin Vergara
# Mi Primer Pipeline Automatizado
> Actividad 3, Unidad 4 — DevOps | ICO 8vo semestre

## ¿Qué hace este repositorio?
Este proyecto demuestra el uso de GitHub Actions para implementar
un pipeline de Integración Continua (CI) con un linter automático (Flake8).

## Pipeline configurado
El archivo `.github/workflows/main.yml` se ejecuta en cada push y realiza:
1. Descarga el código del repositorio
2. Instala Python 3.11
3. Instala Flake8 (linter de Python)
4. Ejecuta el linter — si hay errores, bloquea el proceso

## ¿Por qué esto asegura calidad?
El linter actúa como filtro: ningún código con errores de estilo
puede avanzar en el proceso de entrega sin ser corregido primero.

## Historial de Actions
Ver pestaña **Actions**: incluye un fallo intencional (E501 + F841)
corregido exitosamente en el siguiente commit.
