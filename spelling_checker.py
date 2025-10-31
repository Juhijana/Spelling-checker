from tkinter import *
from spellchecker import SpellChecker

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    text = enter_text.get().strip()
    if not text:
        cs_label.config(text="")
        spell_label.config(text="")
        return

    spell = SpellChecker()
    words = text.split()
    corrected_words = []

    for word in words:
        corrected_word = spell.correction(word)
        
        if corrected_word is None:
            corrected_word = word
        corrected_words.append(corrected_word)

    corrected_sentence = " ".join(corrected_words)

    cs_label.config(text="Correct text is :")
    spell_label.config(text=corrected_sentence)

heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

check_button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
check_button.pack()

cs_label = Label(root, text="", font=("poppins", 20), bg="#dae6f6", fg="#364971")
cs_label.place(x=100, y=250)

spell_label = Label(root, text="", font=("poppins", 20), bg="#dae6f6", fg="#364971", wraplength=500, justify="left")
spell_label.place(x=300, y=250)

root.mainloop()
