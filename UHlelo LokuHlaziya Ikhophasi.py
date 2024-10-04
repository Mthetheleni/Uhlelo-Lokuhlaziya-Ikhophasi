from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfile
from tkinter.messagebox import showinfo
from nltk import FreqDist, Text as nltk_text
from nltk.tokenize import RegexpTokenizer

def calcConcord(event=None):
    global top_2
    file = askopenfilename(filetypes=[('Plain Text Files', '*.txt')])
    if file:
        with open(file, 'r', encoding='utf-8', errors='replace') as f:
            text = nltk_text(tokenizer.tokenize(f.read()))

            concord_button = Button(top_2, text='Imvumelwanomagama', command=lambda: calcConcordance(entry_1.get(), text, top_2))
            concord_button.pack(pady=10)

def calcConcordance(word, text, window):
    concordance_list = text.concordance_list(word)
    text_box.delete(1.0, "end")
    counter = 1.0
    if concordance_list:
        for concordance in concordance_list:
            text_box.insert(counter, concordance.line + "\n")
            counter += 1
    else:
        text_box.insert(counter, "No matches found for the word: {}".format(word))
    window.destroy()

def chooseStudyCorpus():
    global study_corpus_file
    study_corpus_file = askopenfilename(filetypes=[('Plain Text Files', '*.txt')])
    if study_corpus_file:
        showinfo("Information", "Study Corpus file selected: {}".format(study_corpus_file))

def chooseReferenceCorpus():
    global reference_corpus_file
    reference_corpus_file = askopenfilename(filetypes=[('Plain Text Files', '*.txt')])
    if reference_corpus_file:
        showinfo("Information", "Reference Corpus file selected: {}".format(reference_corpus_file))

def open_kn_modal():
    global top_3
    def chooseCorpus():
        global study_corpus_file
        study_corpus_file = askopenfile(mode='r', filetypes=[('Plain Text Files', '*txt')])
        label_1.configure(text="Ikhophasi ekhethiwe: {}".format(study_corpus_file.name), fg='red')

    def chooseReference():
        global reference_corpus_file
        reference_corpus_file = askopenfile(mode='r', filetypes=[('Plain Text Files', '*txt')])
        label_2.configure(text="ikhophasi eyisindlalelo ekhethiwe: {}".format(reference_corpus_file.name), fg='red')
      
    top_3 = Toplevel(root)
    top_3.grab_set()
    top_3.geometry("500x300")
    top_3.title("Ubungqikithimagama")
    global label_1
    label_1 = Label(top_3, text="Khetha ikhophasi", font=('Helvetica', 10), pady=10)
    label_1.pack()
    button_1 = Button(top_3, text='Vula ikhophasi', command=chooseCorpus)
    button_1.pack()
    global label_2
    label_2 = Label(top_3, text="Khetha ikhophasi eyisindlalelo", font=('Helvetica', 10), pady=10)
    label_2.pack()
    button_2 = Button(top_3, text='Vula ikhophasi', command=chooseReference)
    button_2.pack()
    label_3 = Label(top_3, text="", font=('Helvetica', 10), pady=10)
    label_3.pack()
    button_3 = Button(top_3, text='Bala ubungqikithimagama', command=lambda: calcKeyness())
    button_3.pack()

def calcKeyness():

            for word in study_freq:
                study_count = study_freq[word]
                reference_count = reference_freq[word] if word in reference_freq else 0

                contingency_table = [[study_count, study_total - study_count],
           , "Please select both the study corpus and reference corpus files.")

root.geometry("1200x800")
root.configure(bg='orange')
root.title('Mthuli Buthelezi')

title = Label(root, bg='orange', fg='#fff',
              text='Uhlelo LwesiZulu lokuHlaziya iKhophasi yesiZulu',
              font=("Helvetica", 12), pady=30)
title.grid(row=0, columnspan=3)

wordlist_button = Button(root, text='UHLUMAGAMA', command=calcWordList)
wordlist_button.grid(row=1, column=0, pady=20)

concord_button = Button(root, text='IMVUMELWANOMAGAMA', command=calcConcord)
concord_button.grid(row=1, column=1, pady=20)

keyness_button = Button(root, text='UBUNGQIKITHIMAGAMA', command=open_kn_modal)
keyness_button.grid(row=1, column=2, pady=20)

text_box = Text(root, height=20, width=150)
text_box.grid(row=3, column=0, columnspan=3)

root.mainloop()
