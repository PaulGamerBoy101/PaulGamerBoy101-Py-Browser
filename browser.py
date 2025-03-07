import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineProfile
from PyQt5.QtCore import QUrl

# Load settings from JSON file
def load_settings():
    try:
        with open("settings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Floorp/11.14.0",
            "theme": "lime",
            "home_page": "https://custom-new-tab-page-12935782.codehs.me/index.html",
            "new_tab_page": "https://custom-new-tab-page-12935782.codehs.me/index.html",
            "search_engine": "https://www.google.com/search?q="
        }

# Save settings to JSON file
def save_settings(settings):
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = load_settings()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Custom PyQt Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent(self.settings["user_agent"])
        self.browser.setUrl(QUrl(self.settings["home_page"]))
        
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
