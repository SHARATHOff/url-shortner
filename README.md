# 🔗 URL Shortener

A simple, elegant web application for shortening long URLs built with Flask and SQLite. Features a modern, responsive UI with copy-to-clipboard functionality.

## ✨ Features

- **URL Shortening**: Convert long URLs into short, manageable links
- **Automatic Protocol Detection**: Automatically adds `https://` if no protocol is specified
- **Collision Prevention**: Ensures unique short codes by checking for duplicates
- **Modern UI**: Clean, responsive design with smooth animations
- **Copy to Clipboard**: One-click copying of shortened URLs
- **SQLite Database**: Persistent storage for URL mappings
- **Error Handling**: Graceful handling of invalid or expired URLs

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip or uv package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/url-shortner.git
   cd url-shortner
   ```

2. **Install dependencies**
   
   Using pip:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000` to start shortening URLs!

## 📁 Project Structure

```
url-shortner/
├── main.py              # Flask application
├── templates/
│   └── index.html       # Frontend template
├── urls.db              # SQLite database
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project configuration
└── README.md           # This file
```

## 🛠️ How It Works

1. **URL Input**: Users enter a long URL in the web form
2. **Protocol Handling**: The app automatically adds `https://` if no protocol is specified
3. **Short Code Generation**: A random 6-character alphanumeric code is generated
4. **Collision Check**: The system ensures the generated code is unique
5. **Database Storage**: The URL mapping is stored in SQLite database
6. **Redirection**: Short URLs redirect users to the original long URLs

## 🎨 UI Features

- **Gradient Background**: Beautiful blue gradient design
- **Card-based Layout**: Clean white container with shadow effects
- **Smooth Animations**: Fade-in effects and hover transitions
- **Responsive Design**: Works on desktop and mobile devices
- **Toast Notifications**: Visual feedback for copy operations

## 🔧 Configuration

The application uses the following default settings:

- **Database**: `urls.db` (SQLite)
- **Short Code Length**: 6 characters
- **Port**: 5000 (Flask default)
- **Debug Mode**: Enabled for development

## 📊 Database Schema

The application uses a simple SQLite table:

```sql
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    short_url TEXT NOT NULL UNIQUE
)
```

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment
For production deployment, consider:

1. **Disable debug mode** in `main.py`
2. **Use a production WSGI server** like Gunicorn
3. **Set up environment variables** for configuration
4. **Use a production database** like PostgreSQL

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/SHARATHOff/url-shortner/issues) page
2. Create a new issue with detailed information
3. Include steps to reproduce any bugs

## 🔮 Future Enhancements

- [ ] Custom short URL aliases
- [ ] URL analytics and click tracking
- [ ] Bulk URL shortening
- [ ] API endpoints for programmatic access
- [ ] User authentication and personal URL management
- [ ] URL expiration dates
- [ ] QR code generation

---

Made with ❤️ using Flask and modern web technologies.
