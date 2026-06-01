---
name: observable-notebooks
description: Observable notebook workflow guide. Use when Codex needs Observable guidance for notebooks, reactive cells, JavaScript or Observable JavaScript, standard library, Inputs, imports, require, visibility, Markdown, HTML, SQL, data tables, charts, TeX, file attachments, cloud files, databases, database clients/proxies, saving/history, collaboration, sharing, comments, forking, templates, embeds, private notebooks, schedules, notifications, secrets, Plot, D3, or lightweight interactive visualization.
---

# Observable Notebooks

## Overview

Use Observable when the desired artifact is a reactive web-native notebook, interactive chart, lightweight public/private dashboard, or reusable JavaScript visualization.

## Workflow

1. Break the analysis into named cells: data load, normalization, metric computation, chart, controls, and notes.
2. Use Observable Plot for standard charts; use D3 only when Plot cannot express the required interaction or layout.
3. Use Inputs for controlled exploration, not for decorative UI.
4. Use SQL, database, cloud file, attachment, or API cells based on the data source and permission model.
5. Use imports/forks/templates for reuse; preserve source notebooks when adapting community work.
6. Treat sharing, embeds, private access, secrets, and database proxy choices as part of the deliverable.

## Common Tasks

- Notebook authoring: cells, JavaScript, Observable JavaScript, Markdown, HTML, TeX, standard library.
- Data access: file attachments, cloud files, databases, database pane, self-hosted proxies, database clients, secrets.
- Visualization: data table, chart cells, Observable Plot, D3, Inputs.
- Reuse/share: imports, require, templates, forking, collections, embeds, React embeds, custom URLs.
- Operations: saving, history, collaboration, comments, private notebooks, schedules, notifications, security model.

## References

- Read `references/docs-map.md` for official docs coverage.
- Read `references/workflows.md` for notebook and lightweight visualization recipes.
