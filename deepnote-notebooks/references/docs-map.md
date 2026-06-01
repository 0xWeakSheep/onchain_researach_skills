# Deepnote Official Docs Map

Sources:

- Getting started: https://deepnote.com/docs/getting-started
- SQL blocks: https://deepnote.com/docs/sql-cells
- Chart blocks: https://deepnote.com/docs/chart-blocks
- Scheduling: https://deepnote.com/docs/scheduling
- Deepnote API: https://deepnote.com/docs/deepnote-api
- Public API v2 reference: https://deepnote.com/docs/api-reference

## Product Surface

- Getting started: welcome, first steps, workspaces, notebooks, projects, data apps.
- Deepnote Open Source: local setup, Deepnote format, notebook conversion, `.ipynb` migration, notebook organization, VS Code extension.
- Integrations: warehouses/lakes, databases, cloud files, collaboration tools, data processing, machine learning services.
- AI: Deepnote Agent, Deepnote AI, custom AI models, generative analysis, SQL generation, code completion, code editing, data visualization, error fixing, code explanation, custom instructions, prompting tips, data privacy.
- Files: integrated file system, shared datasets, Jupyter notebooks, GitHub imports.
- Notebook blocks: SQL blocks, chart blocks, big number blocks, text editing, input blocks, modules, IPyWidgets, data tables.
- Environment: hardware, dependencies, default/custom environments, project initialization, own kernel, Conda, long-running jobs, variable restore, incoming connections.
- Secrets: environment variables and SSH keys.
- Developer productivity: schema browser, SQL query caching, shortcuts, command palette, execution modes, code intelligence, terminal, variable explorer, dark mode.
- Shipping: apps, scheduling, PDF/project export, launch repositories, Streamlit apps.
- Versioning: version history, Git export, GitLab, Azure Repos, Bitbucket.
- Collaboration: workspace permissions, data catalog, sharing, real-time collaboration, comments, code reviews, block embedding, notebook locking, app/notebook usage insights.
- Security and administration: plans/billing, billing alerts/limits, security overview, SSO/directory sync, audit log, securing connections.
- API: Deepnote API and Public API v2 reference.

## Data Connections

- Warehouses and lakes: Snowflake, Snowpark, Google BigQuery, Amazon Redshift, Amazon Athena, ClickHouse, Trino, Dremio, Databricks.
- Databases: PostgreSQL, MySQL/MariaDB, MongoDB, Microsoft SQL Server/Azure SQL, Supabase, InfluxDB, Google AlloyDB, Google Spanner, Materialize, Google Cloud SQL.
- Cloud files: Amazon S3, Google Cloud Storage, Google Drive, Dropbox, Microsoft OneDrive, Microsoft Azure Blob Storage.
- Collaboration/productivity: Slack, Notion, Airtable, Telegram.
- Processing/ML: dbt, Spark, Great Expectations, ETL/ELT pipelines, MindsDB, Weights & Biases, Comet.ml, Neptune.ai.

Use these integrations for onchain work when raw data lives in a warehouse, offchain labels are in a database, exports are in cloud files, or scheduled reports need Slack notifications.

## SQL Blocks

- SQL blocks run inside Python notebooks.
- SQL blocks query databases, warehouses, CSV files, Excel files, DataFrames, and uploaded/local tabular files.
- After execution, results are stored as a Pandas DataFrame by default and can be used by later Python blocks.
- DataFrame SQL uses DuckDB under the hood.
- Output modes:
  - `DataFrame`: loads the full query result into a Pandas DataFrame.
  - `Query preview`: retrieves the first 100 rows, keeps the SQL source, and supports query chaining without pulling full results into memory.
- Query chaining references query preview objects in later SQL blocks; Deepnote compiles them into CTEs.
- Query chaining only supports single `SELECT` statements; `INSERT`, `UPDATE`, and `DELETE` are not supported.
- Query caching can reduce warehouse load for repeated SQL blocks.
- SQL autocomplete combines schema suggestions and AI completions.
- Python variables can be passed into SQL with JinjaSQL syntax such as `{{ variable_name }}`.
- Use `inclause` for lists/tuples and `sqlsafe` for injected table or column names.
- Handle optional inputs with Jinja conditionals or SQL `NULL` logic.

## Chart Blocks

- Chart blocks create no-code charts from Pandas DataFrames for fast exploratory analysis.
- Add chart blocks from a DataFrame output table's Visualize action or from the block menu.
- Select a DataFrame, chart type, dimensions, measures, and optional grouping.
- Supported field interpretation includes nominal, temporal, and quantitative data.
- Aggregations include count, distinct, sum, min, max, average, and median.
- Quantitative dimensions can be binned; temporal fields can be grouped by time resolution.
- Grouping adds an additional dimension through color or stacked/side-by-side series.
- Chart AI can propose and edit chart configurations from natural-language prompts.
- Interactive filtering can keep/exclude selected points and can also use conditional filters.
- Combo charts support multiple series, series type changes, and secondary axes where appropriate.
- Custom tooltips can add audit context without cluttering the visible chart.

## Scheduling And Alerts

- Scheduling can run notebooks daily, weekly, monthly, hourly, or by custom cron depending on plan.
- Scheduling is available on Team, Pro, and Enterprise plans; hourly/custom schedules are Enterprise-only in the docs.
- Use schedules for recurring data refresh, dashboard updates, monitoring, and productionized notebook tasks.
- Scheduling can notify success/failure by email or Slack.
- A run is failed if an exception is raised; subsequent blocks do not execute after a failing block.
- Each run creates a run snapshot for reviewing successful or failed executions.
- Scheduled notebooks can act as alerts by raising failures when data checks fail.
- Current documented limitation: one scheduled notebook per project; split across projects when more schedules are needed.

## API

- The classic Deepnote API runs existing notebooks programmatically and is available on Team and Enterprise plans.
- API keys are created under workspace settings and sent as bearer tokens:

```http
Authorization: Bearer INSERT_API_KEY
```

- Public API v2 base URL:

```text
https://api.deepnote.com/v2
```

- Public API v2 is documented as preview; avoid relying on preview behavior in production-critical workflows.
- Public API v2 endpoint groups: Blocks, Docs, Files, Integrations, Me, Notebooks, Projects, Runs, Search, Sessions.
- Use API execution when an external service should trigger an existing notebook run, refresh analysis, or integrate Deepnote into a larger workflow.

## Onchain Analysis Fit

- Use Deepnote when the workflow needs SQL and Python together, AI-assisted notebook iteration, warehouse/database access, scheduled reports, team review, or notebook-to-app delivery.
- Prefer SQL blocks for warehouse queries, decoded event tables, token holder snapshots, transaction extracts, and cohort tables.
- Prefer Python blocks for API enrichment, address normalization, label joins, anomaly detection, chart polish, and report assembly.
- Prefer query preview mode for large warehouse iterations; switch to DataFrame mode when Python needs the full result.
- Prefer chart blocks for quick exploratory plots; use Python plotting when custom annotations, advanced formatting, or reusable chart code is required.
- Store API keys and private connection details in Deepnote secrets/environment variables, not in notebooks.
