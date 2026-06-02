# Tool Routing

Choose the rendering path based on output, privacy, repeatability, and interactivity.

## Routing Table

| Need | Preferred tool | Why |
|---|---|---|
| Quick chart image from safe data | `chart-visualization` | Fast AntV image generation |
| Sensitive/private local data | Local Python, notebook, spreadsheet, or front-end code | Avoids external chart API upload |
| Flowchart or decision tree | Mermaid or FigJam | Best for process and logic diagrams |
| Architecture or pipeline diagram | FigJam or Mermaid | Clear nodes and edges |
| Interactive analysis notebook | Observable Plot, Plotly, Hex, or Deepnote | Reusable exploratory controls |
| Production dashboard | ECharts, Recharts, visx, D3, Observable Plot | Better code ownership |
| Report or slide figure | AntV image, spreadsheet chart, or presentation artifact | Exportable and easy to review |
| Custom network/Sankey | D3, Plotly, ECharts, or AntV if simple | More layout control |

## AntV `chart-visualization`

Use when the user asks to generate a chart image and the dataset is safe to send to the AntV online endpoint.

Supported useful types include `line`, `area`, `bar`, `column`, `scatter`, `pie`, `radar`, `funnel`, `waterfall`, `dual-axes`, `histogram`, `boxplot`, `violin`, `word-cloud`, `sankey`, `treemap`, `network-graph`, `flow-diagram`, `mind-map`, and `spreadsheet`.

Before calling it:

1. Reduce the data to chart-ready rows.
2. Remove secrets, private address notes, and unnecessary raw rows.
3. Include title, axis titles, units, width, and height.
4. Keep a local copy of the chart spec when repeatability matters.

## Mermaid And FigJam

Use Mermaid or FigJam for conceptual visuals rather than metric charts:

- Investigation flow.
- Data pipeline.
- Decision tree.
- Protocol architecture.
- Entity relationship diagram.
- Sequence of API/notebook steps.

## Notebook Or Code Chart

Use code when:

- The user needs a reproducible chart.
- The chart needs interaction, filters, or hover details.
- The data is private.
- The chart will become part of a dashboard.
- The user needs local files instead of hosted image URLs.

## Spreadsheet Or Presentation Chart

Use spreadsheets for simple CSV/Excel workflows and finance-style tables. Use presentations when the output is a report deck or executive summary. Keep source tables near the charts.
