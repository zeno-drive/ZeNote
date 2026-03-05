# ZeNote

A multi-user note-taking web app built with Flask, MongoDB, and Jinja2.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Todo](#todo)
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
│   │   └── routes.py        ← edit, save notes
│   ├── folders/
│   │   ├── __init__.py
│   │   └── routes.py        ← create, delete folders and notes
│   ├── static/css/style.css
│   └── templates/
│       ├── layout.html      ← shared base layout
│       ├── hub.html
│       ├── dashboard.html
│       ├── folder_hub.html
│       ├── note_editor.html
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
| folders | { _id, name, user_id, created_at } |
| notes | { _id, name, content, tags:[], folder_id, user_id, created_at, modified_at } |

## Features

### Done
- [x] Multi-user accounts with secure registration and login
- [x] Password hashing with Werkzeug
- [x] Session management with Flask-Login
- [x] Create and delete folders
- [x] Create, delete, and edit notes
- [x] Notes organized inside folders
- [x] Tag notes for easy categorization
- [x] Dark / Light theme toggle
- [x] Random quotes in footer

### Planned
- [ ] Search notes by title, content, or tags
- [ ] Markdown live preview in note editor
- [ ] Improved CSS styling
- [ ] Deploy to Render
- [ ] Version history for notes

## Todo

### Next Up
- [ ] Fix note link in `folder_hub.html` — clicking a note should open `/note_editor/<note_id>`
- [ ] Search route — query notes by title or content using MongoDB text indexes
- [ ] Add Markdown live preview using `marked.js`

### Backlog
- [ ] CSS overhaul — style forms, buttons, and layout properly
- [ ] Deploy to Render with Gunicorn
- [ ] Add `Procfile` for Render deployment
- [ ] Version history — store previous note content on each save
- [ ] Sharing — allow folders or notes to be shared between users

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

Register an account at `/register`, then log in at `/login`. From the dashboard you can create folders. Click a folder to open it and create notes inside. Click a note to open the editor and start writing. The theme toggle in the navbar switches between light and dark mode.

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

- v0.1.0 — Auth, folders, notes CRUD complete

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