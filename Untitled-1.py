from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,  
    QPushButton, QRadioButton,
    QHBoxLayout, QVBoxLayout, 
    QLabel, QGroupBox, QButtonGroup)
from random import shuffle

# Класс вопрос с ответами
class Question():
    def __init__(self, question, r_answer, wrong1, wrong2, wrong3):
        self.question = question

# Создание окна
app = QApplication([])
memo_win = QWidget()
memo_win.setWindowTitle("Memory Card")
memo_win.resize(400, 300)

# Добавляем виджеты
lb_question = QLabel("Здесь будет вопрос")
radio_Group_Box = QGroupBox("Вопрос")
rbtn1 = QRadioButton("Вариант 1")
rbtn2 = QRadioButton("Вариант 2")
rbtn3 = QRadioButton("Вариант 3")
rbtn4 = QRadioButton("Вариант 4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

btn_Ok = QPushButton("Ответить")

# Размещение виджетов в GroupBox
layout_radio1 = QHBoxLayout()
layout_radio2 = QVBoxLayout()
layout_radio3 = QVBoxLayout()

layout_radio2.addWidget(rbtn1)
layout_radio2.addWidget(rbtn2)
layout_radio3.addWidget(rbtn3)
layout_radio3.addWidget(rbtn4)

layout_radio1.addLayout(layout_radio2)
layout_radio1.addLayout(layout_radio3)
radio_Group_Box.setLayout(layout_radio1)

# Создание второго контейнера с ответом
AnsGroupBox = QGroupBox("Результаты")
lb_Result = QLabel("Прав ты или нет?")
lb_Correct = QLabel("Ответ будет тут")
layout_answer = QVBoxLayout()
layout_answer.addWidget(lb_Result, alignment= Qt.AlignLeft | Qt.AlignTop)
layout_answer.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_answer)

# Размещение виджетов в окне программы
main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()

h1_layout.addWidget(lb_question, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
h2_layout.addWidget(radio_Group_Box)
h2_layout.addWidget(AnsGroupBox)
AnsGroupBox.hide()
h3_layout.addStretch(1)
h3_layout.addWidget(btn_Ok, stretch=2)
h3_layout.addStretch(1)

main_layout.addLayout(h1_layout, stretch=2)
main_layout.addLayout(h2_layout, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(h3_layout, stretch=1)
main_layout.addStretch(1)
main_layout.setSpacing(5)
memo_win.setLayout(main_layout)

def show_result():
    radio_Group_Box.hide()
    AnsGroupBox.show()
    btn_Ok.setText("Следующий вопрос")

def show_question():
    AnsGroupBox.hide()
    btn_Ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    radio_Group_Box.show()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(question, right_ans, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_ans)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_question.setText(question)
    lb_Correct.setText(right_ans)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers [3].isChecked():
            show_correct("Неверно!")

def show_correct(res):
    lb_Result.setText(res) 
    show_result()  

ask("Какой национальности не существует?", "Смурфы", "Энцы", "Алеуты", "Чулымцы")
btn_Ok.clicked.connect(check_answer)
memo_win.show()
app.exec_()