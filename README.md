# vecnotes

Search my markdown notes by meaning, not keywords

Side project, maintained when I have time.

## Features

- sentence-transformers when available, TF-IDF fallback
- Vectors cached to .npy so re-runs are instant
- Interactive REPL and one-shot modes
- Reranks by recency when scores tie

## Getting started

```bash
pip install -r requirements.txt
```

## Usage

```bash
python search.py ./notes
>> how do I back up my database?
```

## Project structure

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   ├── workflows/
│   │   └── ci.yml
│   ├── dependabot.yml
│   └── pull_request_template.md
├── docs/
│   ├── configuration.md
│   ├── roadmap.md
│   └── usage.md
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
├── requirements.txt
└── search.py
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## 说明

个人练习项目, 谨慎用于生产环境。

## License

MIT. Do whatever you want.
