from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

app = QApplication(sys.argv)

# Create your main window
window = QWidget()
window.setWindowTitle('Pop-up Styled with QSS')

layout = QVBoxLayout()

label = QLabel('This is a pop-up styled with Qt Style Sheets (QSS)')
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

window.setLayout(layout)
window.resize(400, 200)
window.show()

sys.exit(app.exec_())
