# 🌟 ShareSpace - Social Media Platform

A modern, responsive social media platform built with Django and Tailwind CSS. Share your thoughts, moments, and experiences with a beautiful, mobile-first design.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-v5.2.4+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 🎨 **Modern UI/UX**
- **Professional Dark Theme** - Sleek, modern interface with gradient accents
- **Fully Responsive Design** - Perfect experience on mobile, tablet, and desktop
- **Tailwind CSS Styling** - Clean, utility-first CSS framework
- **Mobile-First Approach** - Optimized for mobile devices with touch-friendly interactions

### 📱 **Mobile Responsive**
- **Adaptive Grid Layout** - 1-4 columns based on screen size
- **Hamburger Menu** - Collapsible navigation for mobile devices
- **Touch-Optimized** - Large tap targets and smooth interactions
- **Progressive Enhancement** - Works great on all devices

### 🔐 **User Authentication**
- **User Registration** - Clean signup process
- **Secure Login/Logout** - Django's built-in authentication
- **Session Management** - Persistent user sessions
- **User Profiles** - Personalized user experience

### 📝 **Post Management**
- **Rich Post Creation** - Title, content, description, and image uploads
- **Image Support** - Upload and display images with posts
- **Privacy Controls** - Public/Private post visibility
- **CRUD Operations** - Create, Read, Update, Delete posts
- **Character Counting** - Real-time character limits with visual feedback

### 🔒 **Privacy & Security**
- **Protected Image Serving** - Secure image access for private posts
- **Permission-Based Access** - Users can only edit/delete their own posts
- **Privacy Badges** - Clear visual indicators for post visibility
- **Custom Error Pages** - Beautiful 404, 403, and 500 error handling

### 🎯 **Advanced Features**
- **Clickable Cards** - Navigate to detailed post views
- **Hover Effects** - Interactive UI elements with smooth transitions
- **Auto-Resize Textareas** - Dynamic form field sizing
- **File Upload Preview** - Visual feedback for image uploads
- **Empty States** - Helpful messages when no content is available

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Django 5.2.4+
- Virtual Environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sharespace.git
   cd sharespace
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   cd FullStack
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
ShareSpace/
├── FullStack/
│   ├── FullStack/           # Main project settings
│   │   ├── settings.py      # Django settings
│   │   ├── urls.py          # Root URL configuration
│   │   └── wsgi.py          # WSGI configuration
│   ├── tweet/               # Main app directory
│   │   ├── models.py        # Database models
│   │   ├── views.py         # View functions
│   │   ├── forms.py         # Django forms
│   │   ├── urls.py          # App URL patterns
│   │   ├── admin.py         # Admin configuration
│   │   └── templates/       # HTML templates
│   │       └── tweet/
│   │           ├── tweet_list.html     # Home page
│   │           ├── tweet_detail.html   # Post detail
│   │           ├── tweet_form.html     # Create/Edit form
│   │           └── tweet_confirm_delete.html
│   ├── templates/           # Global templates
│   │   ├── layout.html      # Base template
│   │   ├── 404.html         # Custom 404 page
│   │   ├── 403.html         # Custom 403 page
│   │   └── 500.html         # Custom 500 page
│   ├── media/               # User uploaded files
│   ├── static/              # Static files
│   └── manage.py            # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🛠️ Technology Stack

### Backend
- **Django 5.2.4** - High-level Python web framework
- **Python 3.11** - Programming language
- **SQLite** - Database (default, easily configurable)
- **Pillow** - Python Imaging Library for image processing

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **HTML5** - Modern markup language
- **JavaScript** - Interactive frontend functionality
- **Responsive Design** - Mobile-first approach

### Features
- **Django ORM** - Object-relational mapping
- **Django Forms** - Form handling and validation
- **Django Authentication** - User management system
- **File Upload Handling** - Image upload and serving
- **Custom Error Pages** - Enhanced user experience

## 📱 Responsive Design

### Breakpoints
- **Mobile** (< 768px): Single column layout
- **Tablet** (768px - 1279px): Two column layout
- **Desktop** (1280px - 1535px): Three column layout
- **Large Desktop** (> 1536px): Four column layout

### Mobile Features
- Hamburger menu navigation
- Touch-friendly buttons
- Optimized image sizes
- Swipe-friendly interfaces
- Compact content display

## 🎨 UI Components

### Cards
- Hover effects with scale animations
- Privacy badges (Public/Private)
- Clickable entire card area
- Responsive image handling
- Action buttons (Edit/Delete)

### Forms
- Real-time character counting
- File upload with preview
- Auto-resizing textareas
- Validation feedback
- Mobile-optimized inputs

### Navigation
- Responsive hamburger menu
- Smooth transitions
- User authentication status
- Mobile-friendly dropdowns

## 🔐 Security Features

- **CSRF Protection** - Cross-site request forgery protection
- **User Permission Checks** - Users can only modify their own content
- **Protected Media Serving** - Secure image access for private posts
- **Input Validation** - Form data validation and sanitization
- **Custom Error Handling** - Secure error page display

## 🚦 Usage

### Creating Posts
1. Click "Create New Post" button
2. Fill in title, content, and optional description
3. Upload an image (optional)
4. Choose privacy setting (Public/Private)
5. Click "Publish Post"

### Managing Posts
- **View**: Click on any post card to see details
- **Edit**: Click edit button on your own posts
- **Delete**: Click delete button with confirmation
- **Privacy**: Toggle between public and private posts

### User Authentication
- **Register**: Create new account with username and password
- **Login**: Access your account
- **Logout**: Secure session termination

## 📊 Database Schema

### Tweet Model
```python
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=280)
    description = models.TextField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## 🎯 Future Enhancements

- [ ] **User Profiles** - Extended user information and avatars
- [ ] **Like/Dislike System** - Post engagement features
- [ ] **Comments** - User interaction on posts
- [ ] **Following System** - User-to-user relationships
- [ ] **Real-time Notifications** - WebSocket integration
- [ ] **Search Functionality** - Find posts and users
- [ ] **Hashtags** - Post categorization
- [ ] **API Development** - REST API for mobile apps
- [ ] **Social Login** - OAuth integration (Google, GitHub)
- [ ] **Email Verification** - Enhanced security

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django community for the excellent framework
- Tailwind CSS for the utility-first CSS approach
- Contributors and testers
- Open source community

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/sharespace/issues) page
2. Create a new issue if needed
3. Contact the maintainer

---

⭐ **Don't forget to star this repository if you found it helpful!**

## 📸 Screenshots

### Desktop View
![Desktop Screenshot](screenshots/desktop-view.png)

### Mobile View
![Mobile Screenshot](screenshots/mobile-view.png)

### Post Creation
![Create Post](screenshots/create-post.png)

### Post Detail
![Post Detail](screenshots/post-detail.png)

---

Made with ❤️ using Django and Tailwind CSS
