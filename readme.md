# ZeNote

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [Testing](#testing)
- [Changelog](#changelog)
- [License](#license)
- [Contact](#contact)

## Overview
### folder overview
notetaking-app/
│
├── app/
│   ├── __init__.py          ← creates the Flask app
│   ├── config.py            ← secret key, MongoDB URI, etc.
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py        ← register, login, logout
│   │
│   ├── notes/
│   │   ├── __init__.py
│   │   └── routes.py        ← create, read, edit, delete notes
│   │
│   ├── folders/
│   │   ├── __init__.py
│   │   └── routes.py        ← create, delete folders
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   └── templates/
│       ├── base.html        ← shared layout
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── notes/
│       │   ├── index.html
│       │   ├── view.html
│       │   └── edit.html
│       └── folders/
│           └── index.html
│
├── .env                     ← secrets, never commit this
├── .gitignore
├── requirements.txt
└── run.py                   ← entry point
### schema

users:   { _id, name, email, hash }
folders: { _id, name, user_id }
notes:   { _id, title, content, tags:[], folder_id, user_id, created_at, updated_at }
## Features

## Getting Started

### Prerequisites

### Installation

## Usage

## Configuration

## API Reference

## Contributing

## Testing

## Changelog

## License

## Contact

---

## Common Markdown Symbols Reference

| Symbol | Syntax | Result |
|--------|--------|--------|
| Heading 1 | `# Heading` | Large title |
| Heading 2 | `## Heading` | Section title |
| Heading 3 | `### Heading` | Sub-section title |
| Bold | `**text**` | **text** |
| Italic | `*text*` | *text* |
| Bold + Italic | `***text***` | ***text*** |
| Strikethrough | `~~text~~` | ~~text~~ |
| Inline Code | `` `code` `` | `code` |
| Code Block | ` ```language ``` ` | Fenced code block |
| Blockquote | `> text` | Indented quote |
| Horizontal Rule | `---` | Divider line |
| Unordered List | `- item` or `* item` | Bullet list |
| Ordered List | `1. item` | Numbered list |
| Checkbox | `- [ ] task` | ☐ Unchecked task |
| Checked Box | `- [x] task` | ☑ Checked task |
| Link | `[text](url)` | Clickable link |
| Image | `![alt](url)` | Embedded image |
| Table | `\| col \| col \|` | Table layout |
| Footnote | `text[^1]` | Footnote reference |
| Escape Character | `\*` | Literal symbol |