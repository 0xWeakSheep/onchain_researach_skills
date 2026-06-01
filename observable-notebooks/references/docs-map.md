# Observable Official Docs Map

Sources:

- Main documentation: https://observablehq.com/documentation/
- Notebooks: https://observablehq.com/documentation/notebooks/
- LLM summary: https://observablehq.com/llms.txt
- Plot: https://observablehq.com/plot/
- D3: https://d3js.org/
- Inputs: https://github.com/observablehq/inputs

## Notebook Docs Coverage

- Notebooks: interactive, editable documents made from cells.
- Cells: JavaScript, Observable JavaScript, standard library, Inputs, imports, require, awaiting visibility, Markdown, HTML, SQL, data table, chart, TeX.
- Data: file attachments, cloud files, databases, database pane, self-hosted proxies, database clients.
- Editing: saving, history, keyboard shortcuts, tinker mode, safe mode, minimap, AI Assist, trash.
- Collaboration: sharing, comments, forking, templates, suggestions, custom URLs, pause live edits, licenses, transfer.
- Organization and delivery: collections, search, embeds, advanced embeds, private notebooks, React embeds, schedules, notifications.
- Security: security model, data access, database proxy, secrets.
- Workspaces: accounts, setup, team, settings, billing, custom SSO, audit logs.
- Related products/docs: Observable Framework, Observable Plot, D3, Observable Inputs, Canvases, Data Apps.

## Core Notebook Model

- A notebook combines Markdown, JavaScript, SQL, HTML, outputs, data tables, charts, and interactive controls.
- Cells are reactive; named cells can be referenced by other cells.
- Use imports to reuse named cells from other notebooks.
- Use file attachments, cloud files, databases, or APIs for data access.
- Use comments, history, sharing, forking, templates, and collections for collaboration and reuse.

## Visualization Stack

- Use Observable Plot for common chart types and fast customization.
- Use D3 when custom layout, marks, interaction, or lower-level control is required.
- Use Inputs for sliders, dropdowns, tables, buttons, text input, and controlled exploration.
- Use chart cells or data tables for fast notebook-native outputs.
- Keep chart design minimal here: correct data shape, encoding, labels, and interaction matter more than custom styling.

## Data and Security

- File attachments and cloud files are suitable for static or managed data files.
- Database connections can use the database pane, database clients, or proxies.
- Use secrets for credentials; do not hardcode API keys in cells.
- Private notebooks, embeds, and data access rules must be considered before sharing external-facing work.

## Embedding and Operations

- Use embeds for publishing notebooks or specific outputs outside Observable.
- Use advanced embeds or React embeds when integrating into applications.
- Use schedules and notifications for recurring notebook refreshes.
- Use history/safe mode when debugging broken notebooks.
