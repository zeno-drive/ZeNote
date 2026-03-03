# ZeNote

A multi-user note-taking web app built with Flask, MongoDB, and Jinja2.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)
- [Contact](#contact)

## Overview

ZeNote is a web-based note-taking application that supports multiple users with secure authentication. Users can organize notes into folders, tag them for easy retrieval, and search across their content.

### Project Structure

```
ZeNote/
├── app/
│   ├── __init__.py          ← creates the Flask app
│   ├── config.py            ← secret key, MongoDB URI
│   ├── models.py            ← User class, validators, quotes
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py        ← register, login, logout
│   ├── notes/
│   │   ├── __init__.py
│   │   └── routes.py        ← create, read, edit, delete notes
│   ├── folders/
│   │   ├── __init__.py
│   │   └── routes.py        ← create, delete folders
│   ├── static/css/style.css
│   └── templates/
│       ├── layout.html      ← shared base layout
│       ├── hub.html
│       ├── dashboard.html
│       ├── register.html
│       └── login.html
├── .env                     ← secrets, never commit
├── .gitignore
├── requirements.txt
└── run.py                   ← entry point
```

### Database Schema

| Collection | Fields |
|------------|--------|
| users | { _id, name, email, hash } |
| folders | { _id, name, user_id } |
| notes | { _id, title, content, tags:[], folder_id, user_id, created_at, updated_at } |

## Features

- Multi-user accounts with secure registration and login
- Password hashing with Werkzeug
- Session management with Flask-Login
- Organize notes into folders
- Tag notes for easy categorization
- Search across notes
- Dark / Light theme toggle
- Random quotes in footer

## Getting Started

### Prerequisites

- Python 3.10+
- MongoDB Atlas account (or local MongoDB)
- pip and virtualenv

### Installation

1. Clone the repository:
```bash
git clone https://github.com/zeno-drive/ZeNote.git
cd ZeNote
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net/zenote
SECRET_KEY=your_secret_key_here
```

5. Run the app:
```bash
python run.py
```

## Usage

Register an account at `/register`, then log in at `/login`. From the dashboard you can create folders and notes, tag content, and search across your notes. The theme toggle in the navbar switches between light and dark mode.

## Configuration

All configuration is loaded from the `.env` file via `app/config.py`. Required variables:

- `MONGO_URI` — MongoDB connection string
- `SECRET_KEY` — Random secret string for session signing

## Tech Stack

- Python Flask
- Jinja2
- MongoDB Atlas
- Flask-PyMongo
- Flask-Login
- Werkzeug
- Bootstrap 5
- python-dotenv
- email-validator

## Contributing

Pull requests are welcome. For major changes please open an issue first.

## Changelog

- v0.1.0 — Initial release: auth, folders, notes, search

## License

MIT

## Contact

GitHub: https://github.com/zeno-drive/ZeNote

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