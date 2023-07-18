from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

## ウィンドウの作成と設定
# Tkクラスのインスタンスを作成、ルートウィンドウを作成
root=Tk()
# ルートウィンドウのタイトル設定
root.title("Python IDLE")
# ルートウィンドウのサイズと位置
root.geometry("1280x720+150+80")
# ルートウィンドウの背景色を設定
root.configure(bg="#323846")
# ルートウィンドウのサイズ変更を禁止
root.resizable(False,False)

# ファイルパスを格納するための変数を初期化
file_path=''

# ファイルパスを設定するための関数
def set_file_path(path):
    global file_path
    file_path=path

# ファイルを開くための関数
# askopenfilenameダイアログを表示し
# 選択されたファイルの内容を読み取り、テキストボックスに表示
def opne_file():
    path = askopenfilename(filetypes=[('Python Files','py')])
    with open(path,'r',encoding='utf-8',errors='ignore') as file:
        code=file.read()
        code_input.delete('1.0',END)
        code_input.insert('1.0',code)
        set_file_path(path)

# ファイルを保存するための関数
# ファイルが指定されていない場合はasksaveasfilenameダイアログを表示
# ファイルが指定されている場合は既存のファイルパスを使用
def save():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('Python Files','py')])
    else:
        path=file_path

    with open(path,'w') as file:
        code = code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)

# ファイルを実行するための関数
# ファイルが保存されていない場合はエラーメッセージボックスを表示
# 保存されている場合は指定されたファイルをpythonコマンドとして実行、出力
def run():
    if file_path =='':
        messagebox.showerror("Python IDLE","Save Your Code")
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    output , error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',error)


# アイコンの設定
# ロゴ画像を読み込み、image_icon変数に代入
image_icon=PhotoImage(file="logo.png")
# ルートウィンドウのアイコンを設定
root.iconphoto(False,image_icon)


# コード入力領域の作成
# テキストボックス(code_input)を作成、フォントとサイズも指定
code_input = Text(root,font="consolas 18")
# テキストボックスをウィンドウ内の指定された位置に配置
code_input.place(x=180,y=0,width=680,height=720)

# 出力結果の作成
# テキストボックス(code_output)を作成
# フォント、サイズ、背景色、テキストの色も指定
code_output = Text(root,font="consolas 15",bg="#323846",fg="lightgreen")
# テキストボックスをウィジェット何の指定された位置に配置
code_output.place(x=860,y=0,width=420,height=720)


# ボタンの作成
# ボタン用の画像(open.png)を読み込み、Open変数に代入
# 以下二つ同じ
Open=PhotoImage(file="open.png")
Save=PhotoImage(file="save.png")
Run=PhotoImage(file="run.png")

# ボタンを作成し、指定された位置に配置
# ボタンがクリックされたときにopen_file関数が実行
# 以下二つ同じ
Button(root,image=Open,bg="#323846",bd=0,command=opne_file).place(x=30,y=30)
Button(root,image=Save,bg="#323846",bd=0,command=save).place(x=30,y=145)
Button(root,image=Run,bg="#323846",bd=0,command=run).place(x=30,y=260)

root.mainloop()
