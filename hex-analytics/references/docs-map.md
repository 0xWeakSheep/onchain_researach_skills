# Hex Official Docs Map

Sources:

- Main docs: https://learn.hex.tech/docs
- SQL cells: https://learn.hex.tech/docs/explore-data/cells/sql-cells/sql-cells-introduction
- Chart cells: https://learn.hex.tech/docs/explore-data/cells/visualization-cells/chart-cells
- Public API: https://learn.hex.tech/docs/api-integrations/api/overview
- Dune connector reference: https://docs.dune.com/api-reference/connectors/trino/hex.md

## Top-Level Docs Coverage

- Getting started: what Hex is, connect data, create first project, develop notebook, share work, AI in Hex.
- Connect to data: data connections, semantic models, uploads, cloud storage, import data via API.
- Analyze and build: projects, notebook view, cells, threads, chat with app, components, data browser.
- Agent management: Context Studio, observability, suggestions, context management, agent personalization.
- Share insights: apps, scheduled runs, app notifications, Explore, embedding, Hex Agent in Slack.
- Collaborate: sharing/permissions, comments, real-time collaboration, reviews.
- Find and organize: workspace search, projects, collections, statuses/categories, owners, archive.
- Administration: user settings, workspace settings, SSO, credits, billing.
- API and integrations: CLI, MCP server, external apps, Slack, integration data connection access, Public API.
- Trust and legal: data privacy, AI data privacy, terms.

## SQL Cells

- Use warehouse SQL for data that lives in a warehouse or Dune Trino connection.
- Use dataframe SQL for CSVs, uploaded files, Python-mutated dataframes, or joins across different data sources.
- Use query mode for large datasets, especially around or above 100k rows, to reduce streaming and memory pressure.
- Query mode returns a preview instead of the full result and pushes compatible no-code transformations to the warehouse.
- Use dataframe mode when Python cells need the full result or the dataset is small.
- Hex SQL execution is reactive: downstream cells rerun when upstream cells or Jinja parameters change unless run behavior is changed.
- Hex can run independent cells in parallel.
- SQL query caching can avoid repeated warehouse execution.
- Multi-statement queries must be in one SQL cell if they require a shared database session; Athena, Databricks, ClickHouse, and Trino do not support multi-statement queries in this context.

## Cell Families

- Python cells.
- SQL cells: introduction, formatting, query caching.
- Text cells.
- Transform cells: pivot and related no-code transformations.
- Visualization cells: chart, table display, single value, map.
- Input cells: parameters and app controls.
- Data cells: dbt metrics and other data-source aware cells.
- Calculations, Jinja, typeahead.

## Chart Cells

- Chart cells visualize dataframes and SQL query results with no-code charts.
- Key concepts: dimensions, measures, aggregation, color-by, scale type, ordering, multi-series, dual Y-axis, faceting, data labels, reference lines, joins, output dataframe, interactive filtering.
- Use chart output dataframes when downstream cells need the filtered or aggregated chart result.
- Joins in chart cells are database-table oriented; validate join keys and cardinality warnings.
- Keep chart design minimal in this skill: correct metric, grouping, unit, date handling, and caveat matter more than styling.

## Public API

Authentication concepts:

- Personal access tokens.
- Workspace tokens.
- Token expiration.
- Valid base URL and authorization header are required.

Common API tasks:

- Run a published project with default inputs.
- Run a published project with custom inputs.
- Update cached state and query cache.
- Create groups from user emails.
- Create collections with sharing permissions.
- Change collection permissions.
- Rotate data connection credentials.
- Cancel active project runs.
- Check kernel and rate limits.

`hextoolkit` helpers:

- Create API client.
- Get project metadata.
- Run project.
- Get run status.
- Cancel run.
- Get project runs with status filters.

Troubleshooting:

- `401`: auth/base URL/token issue.
- `404`: missing resource or insufficient permission.
- `422`: unpublished project or invalid input parameters.
- `429`: request rate limit.
- `500`: Hex application error.
- `503`: kernel/concurrency limit.

## Dune + Hex

Use Dune Trino from Hex when the notebook should query Dune datasets directly. Keep heavy onchain joins in Dune/Trino, use Hex for notebook iteration, stakeholder apps, scheduled runs, parameters, comments, and internal sharing.
