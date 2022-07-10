#モジュールのインポート
import this
import tkinter as tk  
import tkinter.font as font  
import tkinter.messagebox
import datetime 
#メッセージボックスの表示
def massage():
    tkinter.messagebox.showinfo("簡易テキストエディタについて", "シンプルなテキストエディタです。テキストの出力もできます。")
def output():  
    a = text_widget.get("1.0","end")  
    dt = datetime.datetime.today() 
    print(str(dt)+ "・・・テキスト:" + a) 

root = tk.Tk()  
my_font = font.Font(root, family="MS Gothic")  
text_widget = tk.Text(root, wrap= tk.NONE, font=my_font,foreground='white',insertbackground='white') 
text_widget.configure(bg='#000000')  
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))  
root.columnconfigure(0, weight=1)  
root.rowconfigure(0, weight=1)
#スクロールバー  
yscroll = tk.Scrollbar(text_widget, command=text_widget.yview)  
xscroll = tk.Scrollbar(text_widget, command=text_widget.xview,orient=tk.HORIZONTAL)  
yscroll.pack(side=tk.RIGHT, fill = "y")  
xscroll.pack(side=tk.BOTTOM, fill="x")  
text_widget['yscrollcommand'] = yscroll.set  
text_widget['xscrollcommand'] = xscroll.set  
#メニューバー  
menubar = tk.Menu(root, font = my_font)  
filemenu0 = tk.Menu(menubar, tearoff=0)   
filemenu0.add_separator()  
filemenu0.add_command(label=("テキストを出力"),command=output)  
filemenu0.add_separator()  
filemenu0.add_command(label=("メモ帳について"), command=massage) 
filemenu0.add_command(label=("メモ帳の終了(X)"), command= root.quit)  
menubar.add_cascade(label="ファイル(F)", menu=filemenu0)     
root.config(menu=menubar) 


root.title("無題")  
root.geometry("500x250")  
root.mainloop()