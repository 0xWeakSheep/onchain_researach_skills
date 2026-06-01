---
name: hex-analytics
description: Hex analytics notebook and app workflow guide. Use when Codex needs Hex guidance for SQL/Python/no-code notebooks, data connections, semantic models, uploads, cloud storage, API imports, projects, notebook view, cells, components, data browser, AI in Hex, app builder, scheduled runs, notifications, embedding, sharing, collaboration, reviews, workspace administration, CLI, MCP, external apps, public API, or data privacy.
---

# Hex Analytics

## Overview

Use Hex when the desired artifact is a collaborative analysis notebook, stakeholder-facing data app, parameterized report, or SQL/Python workflow connected to warehouses or Dune through Trino.

## Workflow

1. Choose notebook mode for exploration and app mode for stakeholder delivery.
2. Connect data through warehouse, file, cloud storage, API import, semantic model, or Dune Trino connector.
3. Use SQL cells for warehouse pushdown, Python cells for transformation/modeling, no-code chart/pivot/input cells for fast report assembly.
4. Parameterize with input cells only when the stakeholder needs controlled filtering or scenarios.
5. Publish as an app/report when the analysis is stable; keep notebook comments/reviews for analyst iteration.
6. Keep charts simple for now: clean titles, explicit units, sensible aggregation, and visible caveats.

## Common Tasks

- Build: project setup, notebook view, SQL/Python/no-code cells, components, data browser, chat with app.
- Connect: data connections, semantic models, file upload, cloud storage, import via API.
- Share: apps, scheduled runs, app notifications, Explore, embeds, Slack, permissions.
- Collaborate: real-time collaboration, comments, reviews, owners, collections, statuses.
- Operate: user/workspace settings, SSO, credits, CLI, MCP, external apps, public API, privacy.

## References

- Read `references/docs-map.md` for official docs coverage.
- Read `references/workflows.md` for Hex notebook/app recipes.
