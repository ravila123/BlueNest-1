# 🐶 BlueNest - Personal Task Manager

A beautiful, intuitive Streamlit-based todo application designed for personal task management with multi-user support and date-based organization.

## ✨ Features

- **Multi-User Support**: Switch between different users (Ravi, Amitha)
- **Date-Based Organization**: View and manage tasks for specific dates
- **Interactive Checkboxes**: Mark tasks as complete with visual feedback
- **Beautiful UI**: Custom wallpaper background with glassmorphism design
- **Real-time Updates**: Tasks update instantly with checkbox interactions
- **Persistent Storage**: SQLite database for reliable data storage
- **Responsive Design**: Works seamlessly across different screen sizes

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd bluenest-todo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 🐳 Docker Deployment

### Build and Run with Docker

1. **Build the Docker image**
   ```bash
   docker build -f Dockerfile -t bluenest:latest .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 bluenest:latest
   ```

3. **Access the app**
   Open `http://localhost:8501` in your browser

## 📱 How to Use

1. **Select User**: Choose between available users from the sidebar dropdown
2. **Pick Date**: Select the date you want to view/manage tasks for
3. **Add Tasks**: Enter new tasks in the input field and click "Add Task"
4. **Complete Tasks**: Check the checkbox next to any task to mark it as done
5. **View Progress**: Completed tasks show with strikethrough text

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Database**: SQLite
- **Image Processing**: PIL (Python Imaging Library)
- **Styling**: Custom CSS with glassmorphism effects
- **Deployment**: Docker support included

## 📁 Project Structure

```
bluenest-todo/
├── app.py              # Main Streamlit application
├── db_funcs.py         # Database operations and functions
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── data.db            # SQLite database (auto-generated)
├── side art1.png      # Sidebar artwork
├── to-do wallpaper.png # Background wallpaper
└── static/            # Static assets directory
```

## 🎨 Customization

### Changing Background
Replace `to-do wallpaper.png` with your preferred background image.

### Adding Users
Modify the user list in `app.py`:
```python
selected_user = st.sidebar.selectbox("Select User", ["Your", "Users", "Here"])
```

### Styling
Custom CSS can be modified in the `st.markdown()` section of `app.py`.

## 🔧 Database Schema

The app uses a simple SQLite database with the following structure:
- **Tasks Table**: Stores task text, status, and date information
- **Automatic Management**: Database and tables are created automatically on first run

## 🚀 Deployment Options

### Heroku
The app includes a `Procfile` for easy Heroku deployment.

### Streamlit Cloud
Can be deployed directly to Streamlit Cloud by connecting your GitHub repository.

### Local Network
Run locally and access from other devices on your network using your machine's IP address.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Ravi** - *Initial work and development*

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Inspired by modern task management principles
- Custom artwork and design elements

---

⭐ **Star this repository if you find it helpful!**