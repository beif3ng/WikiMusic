# WikiMusic

A Django music encyclopedia with template-based views. Catalog music groups, their albums, songs, and members — complete with image uploads, audio file storage, and full-text search across all entities.

## Features

- Browse and manage music groups, albums, songs, and group members
- Image uploads for groups, albums, and member photos
- Audio file storage per song
- Full-text search across groups, albums, songs, and members
- Template-based UI with dedicated detail and list views for each entity
- Django admin integration

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | Django 5.1 |
| Image handling | Pillow |
| Database | SQLite (default) |

## Data Model

```
Group
 ├──< Album >──< Song
 ├──< Song (standalone)
 └──< GroupMember
```

| Model | Key Fields |
|---|---|
| `Group` | `name`, `description`, `creation_date`, `image` |
| `Album` | `name`, `description`, `group` (FK), `release_date`, `cover_image` |
| `Song` | `name`, `description`, `album` (FK), `group` (FK), `duration`, `audio_file`, `lyrics` |
| `GroupMember` | `name`, `biography`, `role`, `birth_date`, `photo`, `group` (FK) |

## Project Structure

```
WikiMusic/
├── wiki_music/
│   ├── main/
│   │   ├── models.py     # Group, Album, Song, GroupMember
│   │   ├── views.py      # List, detail, and search views
│   │   ├── urls.py
│   │   └── admin.py
│   └── wiki_music/       # Django settings and root URLs
└── requirements.txt
```

## Getting Started

```bash
git clone https://github.com/Nezdeshniy/WikiMusic.git
cd WikiMusic/wiki_music
pip install -r ../requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The app will be available at `http://localhost:8000`.
Admin panel is at `http://localhost:8000/admin/`.

## Pages

| URL | Description |
|---|---|
| `/` | Home page: overview of all groups, albums, songs, and members |
| `/groups/` | Full list of groups |
| `/groups/<id>/` | Group detail with albums and songs |
| `/albums/` | Full list of albums |
| `/albums/<id>/` | Album detail with track listing |
| `/songs/` | Full list of songs |
| `/songs/<id>/` | Song detail with lyrics and audio |
| `/members/` | Full list of group members |
| `/members/<id>/` | Member biography |
| `/search/?q=<query>` | Search across all entities |
