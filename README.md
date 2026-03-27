# 🚀 Sachin's Portfolio - Complete Setup Guide

## 📁 Project Structure & File Connections

```
sachin_project/
├── index.html              (Frontend - Portfolio page)
├── admin.html              (Frontend - Admin dashboard)
├── style.css               (Styling - Both HTML files)
├── script.js               (Frontend Logic - Contact form, visitor count)
├── server.py               (Backend - Flask API server)
├── database.py             (Database - SQLite operations)
├── requirements.txt        (Python dependencies)
├── .env                    (Configuration)
├── portfolio.db            (SQLite database - auto-created)
├── run.bat                 (Windows startup script)
└── images/
    └── profile.jpg         (Profile image)
```

## 🔗 How All Files Are Connected

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  index.html ──────────► style.css (styling)               │
│       │                                                      │
│       └──────────────► script.js (functionality)           │
│                          │                                  │
│                          └─► Sends/Receives from API       │
│                                                              │
│  admin.html ──────────► style.css (styling)               │
│       │                                                      │
│       └──────────────► script.js via HTML                 │
│                          │                                  │
│                          └─► Fetches messages from API     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                            ↓ (HTTP Requests/Responses)
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND LAYER                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  server.py (Flask)                                         │
│  ├── /                    → Serves index.html             │
│  ├── /admin               → Serves admin.html             │
│  ├── /api/contact         → Saves messages                │
│  ├── /api/admin/contacts  → Retrieves all messages        │
│  ├── /api/admin/contacts/<id> → Deletes message          │
│  ├── /api/widgets         → Gets visitor count            │
│  └── /api/portfolio       → Gets portfolio data           │
│       │                                                     │
│       └──────────────► database.py (SQLite)              │
│                          │                                 │
│                          ├── add_contact()                │
│                          ├── get_all_contacts()           │
│                          ├── delete_contact()             │
│                          └── init_database()              │
│                               │                           │
│                               └─► portfolio.db (SQLite)   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Data Flow - Contact Form

```
1. User fills form in index.html
   ↓
2. script.js validates and sends POST to /api/contact
   ↓
3. server.py receives request
   ↓
4. database.py saves to SQLite (portfolio.db)
   ↓
5. Admin visits /admin page
   ↓
6. admin.html fetches messages from /api/admin/contacts
   ↓
7. Messages displayed in admin table
```

## 🛠️ Installation & Setup

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- flask - Web server framework
- python-dotenv - Environment variables

### Step 2: Run the Server

**Option A: Using the startup script (Windows)**
```bash
run.bat
```

**Option B: Manual startup**
```bash
python server.py
```

The server will start at:
- Local: `http://127.0.0.1:5000`
- Network: `http://192.168.0.117:5000` (or your IP)

## 🌐 Access Points

| Page | URL |
|------|-----|
| **Portfolio** | `http://127.0.0.1:5000/` |
| **Admin Panel** | `http://127.0.0.1:5000/admin` |
| **Health Check** | `http://127.0.0.1:5000/health` |

## 📡 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Serve portfolio page |
| GET | `/admin` | Serve admin dashboard |
| POST | `/api/contact` | Submit contact message |
| GET | `/api/admin/contacts` | Get all messages |
| DELETE | `/api/admin/contacts/<id>` | Delete a message |
| GET | `/api/widgets` | Get visitor count |
| GET | `/api/portfolio` | Get portfolio data |
| GET | `/health` | Server health check |

## ✨ Features Implemented

✅ **Contact Form**
- Name, email, message validation
- Messages saved to SQLite database
- Real-time feedback to user

✅ **Admin Dashboard**
- View all received messages
- Search/filter contacts
- Delete individual messages
- Message count stats

✅ **Responsive Design**
- Mobile-friendly layout
- Works on all screen sizes
- Professional styling

✅ **Database**
- SQLite for easy setup (no external DB needed)
- Auto-creates tables on first run
- Persistent storage

## 🐛 Troubleshooting

### Messages Not Saving?
1. Check if `portfolio.db` exists in the folder
2. Verify Python can write to the directory
3. Check server console for errors
4. Ensure all form fields are filled

### Port 5000 Already in Use?
Edit `.env`:
```env
PORT=5001
```
Then restart the server.

### Admin Page Shows No Messages?
1. Submit a test message first from portfolio page
2. Wait a moment for the database to save
3. Refresh the admin page

### Still Not Working?
Run the health check:
```
http://127.0.0.1:5000/health
```
Should return: `{"status": "ok", "message": "Server is running"}`

## 📝 Environment Variables (.env)

```env
FLASK_ENV=development      # Development mode
FLASK_DEBUG=True           # Enable debug mode
PORT=5000                  # Server port
```

## 🔐 Database Info

- **Type:** SQLite
- **File:** `portfolio.db`
- **Tables:**
  - `contacts` - Stores contact messages
  - `visitors` - Tracks visitor count

**No external database setup needed!** SQLite creates everything automatically.

## 📚 File Descriptions

### Frontend Files
- **index.html** - Main portfolio page with all sections
- **admin.html** - Admin panel for managing messages
- **style.css** - CSS styling for both pages
- **script.js** - JavaScript for form handling and API calls

### Backend Files
- **server.py** - Flask application with all routes/APIs
- **database.py** - SQLite database operations
- **requirements.txt** - Python package dependencies
- **.env** - Configuration variables

### Other Files
- **portfolio.db** - SQLite database (auto-created)
- **run.bat** - Windows startup script
- **images/** - Folder for images (profile.jpg)

## ✅ Everything is Now Connected!

All files work together seamlessly:
1. Frontend sends contact form to backend API
2. Backend saves to SQLite database  
3. Admin panel retrieves and displays messages
4. Complete solution with no external dependencies!

## 🚀 Ready to Go!

Your portfolio is now fully functional with:
- Working contact form
- Admin message management  
- Responsive design
- SQLite persistence

Just run your server and start receiving messages! 🎉
- Update `.env` with your database URL if different
- Tables will auto-create when server starts

**Option B: Using SQLite (Default Fallback)**
- No setup needed! SQLite database auto-creates
- Messages stored in `portfolio.db`

### 3. Run the Server
```bash
python server.py
```

Server will start at: `http://localhost:5000`

## 📡 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Main portfolio page |
| `/admin` | GET | Admin dashboard |
| `/api/contact` | POST | Submit contact message |
| `/api/admin/contacts` | GET | Get all messages (admin) |
| `/api/admin/contacts/<id>` | DELETE | Delete a message |
| `/api/widgets` | GET | Get visitor count & quote |
| `/api/portfolio` | GET | Get portfolio data |
| `/health` | GET | Server health check |

## 🔧 Features

✅ Contact form with message submission
✅ Visitor counter
✅ Admin panel to manage messages
✅ Responsive design
✅ Database persistence
✅ Error handling & fallbacks
✅ Profile image with error fallback

## 🛠️ Troubleshooting

### Messages Not Saving?
- Check if PostgreSQL is running: `psql -U postgres`
- Verify `.env` DATABASE_URL is correct
- Check server logs for errors

### Can't Connect to Database?
- Falls back to in-memory storage (MEMORY_MESSAGES)
- Messages will be lost when server restarts
- Set up PostgreSQL for persistent storage

### Port 5000 Already in Use?
- Change PORT in `.env` file
- Restart server with new port

## 📝 Environment Variables (.env)

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/sachin_portfolio
PORT=5000
FLASK_ENV=development
FLASK_DEBUG=True
```

## ✅ Everything is Now Connected!

All files work together to create a complete portfolio website with contact management.
