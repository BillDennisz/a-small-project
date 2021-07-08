import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import work1_fun_conbine as w1fun
from tkinter.font import Font
import traceback
import tkinter.messagebox
import numpy as np
import time
import gettext

# _ = lambda s: s
Current_filepath = os.path.dirname(os.path.abspath(__file__))
Language = gettext.translation('zh_GUI_work1_combine', localedir=os.path.join(Current_filepath, 'locale'), languages=['zh'])
Language.install()


def selectPath():
    path_ = askdirectory()
    path.set(path_)
    # print(path_)

def selectPath_p(path_in):
    path_ = askdirectory()
    path_in.set(path_)
    # print(path_)

def print_entry(self,Entry1):
    if Entry1:
        print(Entry1)
        self.destroy()

def startOUT(filepath):
    print(type(filepath))
    print('The file path is:\n {}'.format(filepath))

def conbine2list(C0,C1,C2,C3,C4,C5,C6):
    listresult=[]
    if C0:
        listresult.append(C0)
    if C1:
        listresult.append('.srt')
    if C2:
        listresult.append(".eng.srt")
    if C3:
        listresult.append('.英文.srt')
    if C4:
        listresult.append('.简体&英文.srt')
    if C5:
        listresult.append('.繁体&英文.srt')
    if C6:
        listresult.append('英文.ass')
    return listresult

window = tk.Tk()
window.geometry('800x640')
window.geometry("800x620+500+110")
window.iconbitmap("file1.ico")

window.minsize(800, 640)
window.maxsize(800, 640)

path = StringVar()
path2 = StringVar()
extension1 = StringVar()
infoshow = StringVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar_index1 = IntVar()
CheckVar_index2 = IntVar()
CheckVar_index3 = IntVar()
CheckVar_index4 = IntVar()
CheckVar_index5 = IntVar()
CheckVar_index6 = IntVar()

class Application(tk.Frame):
    count = 0

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #  各种标签
        self.master.title(_("       Count the number of words per minute in the subtitle file and generate a text file      "))
        self.canvas1 = tk.Canvas(window, width=300, height=110)
        self.canvas1.place(x=510,y=108)
        self.canvas1.create_rectangle(10, 4,255,100,outline = 'gray')
        self.canvas2 = tk.Canvas(window, width=560, height=20)  # bg='pink'
        self.canvas2.place(x=27, y=250)
        self.canvas2.create_rectangle(0, 13, 560, 13.1, fill='gray')
        self.L1=tk.Label(window, text=_('Object path:'))
        self.L1.place(x=10, y=18)
        self.L5 = tk.Label(window, text='350,150')
        self.L5.place(x=350, y=150)
        self.L2 = tk.Label(window, text=_('Output \npath:'))
        self.L2.place(x=10, y=68)
        self.L3 = tk.Label(window, text=_('Customize \nextension:'))
        self.L3.place(x=10, y=118)
        # self.L4 = tk.Label(window, text='by 野鹤无粮\n@2020/03 \nVersion:1.0 ')
        # self.L4.place(x=660, y=540)
        # 文件路径 和 输出文件路径 及选择按钮
        self.L5 = tk.Label(window, text= _('  Information  '))
        self.L5.place(x=285, y=250)
        self.L6 = tk.Label(window, text=_('Option:')) # , bg='blue'
        self.L6.place(x=540, y=115, width=100, height=20)
        self.E1 = tk.Entry(window, textvariable=path, highlightcolor='blue')
        self.E1.place(x=90, y=15, width=540, height=30)

        self.BE1 = tk.Button(window, text=_("Browse"), command=selectPath,background='white')
        self.BE1.place(x=660, y=14)
        self.E2 = tk.Entry(window, textvariable=path2, highlightcolor='blue')
        self.E2.place(x=90, y=70, width=540, height=30)

        self.BE2 = tk.Button(window, text=_("Browse"), command=lambda: selectPath_p(path2), background='white')
        self.BE2.place(x=660, y=70)
        # about extension
        self.E3 = tk.Entry(window, textvariable=extension1, highlightcolor='blue')
        self.E3.place(x=90, y=125, width=200, height=30)
        # to show info
        # self.E4 = tk.Entry(window, textvariable=infoshow, highlightcolor='white')
        # self.E4.place(x=80, y=350, width=400, height=60)
        txtwidth = 560
        txtheight = 320
        txt_x = 30
        txt_y = 280
        self.Text1 = tk.Text(window, wrap='none')
        self.Text1.place(width=txtwidth, height=txtheight, x=txt_x, y=txt_y)
        self.Text1.configure(state='disabled')
        scroll_y = tk.Scrollbar()
        scroll_y.place(width=20, height=txtheight, x=txt_x + txtwidth + 2, y=txt_y)
        scroll_x = tk.Scrollbar(window, orient='horizontal')
        scroll_x.place(width=txtwidth, height=20, x=txt_x, y=txt_y + txtheight + 2)
        self.filename_sum = [];        self.wordnumber_sum = []; self.subtitlerate_sum = [];    self.oldNamelist = [];
        self.newNamelist = [];         self.newNameaddlist = []; self.timecostsum = [];
        # connect
        scroll_y.config(command= self.Text1.yview)
        scroll_x.config(command= self.Text1.xview)
        self.Text1.config(yscrollcommand=scroll_y.set)
        self.Text1.config(xscrollcommand=scroll_x.set)
        self.Text1.tag_config("tag_R", foreground="red")
        self.Text1.tag_config("tag_B", foreground="blue")
        self.Text1.tag_config("tag_G", foreground="green")
        self.Text1.tag_config("tag_gray", backgroun="white", foreground="gray")
        self.Text1.tag_config("tag_orange", foreground="orange")
        self.Text1.tag_config("tag_purple", foreground="purple")
        self.Text1.tag_config("tag_YR", backgroun="yellow", foreground="red")
        self.Text1.tag_config("tag_chocolate", foreground="chocolate")
        self.Text1.tag_config("tag_PaleVioletRed", foreground="PaleVioletRed")
        self.Text1.tag_config("tag_DarkCyan",foreground="DarkCyan")
        self.Text1.tag_config("tag_Tomato", foreground="Tomato")
        self.Text1.tag_config("tag_SaddleBrown", foreground="SaddleBrown")
        myFont = Font(size=10)
        # myFont11 = Font(size=11)
        myFont11 = Font(family="微软雅黑", size=11)
        # myFont = Font(family="Arial", size=12)
        self.Text1.configure(font=myFont)
        self.B2 = tk.Button(window, text=_("Quit"))
        self.B2.place(x=670, y=545,width=80, height=30)
        self.B2["command"] =lambda: self.quitfun()
        self.B3 = tk.Button(window, text=_("Start"), background='blue')
        # self.B3.place(x=450, y=210)
        self.B3["command"] = lambda: self.startIN(self.E1.get())
        self.B5recover = tk.Button(window, text=_("Recover"), highlightcolor='white',width=9, height=1)
        self.B5recover.place(x=660, y=218, width=80, height=30)
        self.B5recover["command"] = lambda: w1fun.renamefun(self.oldNamelist,self.newNamelist,-1, self.Text1)
        self.B5rename = tk.Button(window, text=_("Rename"), highlightcolor='white', width=9, height=1)
        self.B5rename.place(x=550, y=218, width=80, height=30)
        self.B5rename["command"] = lambda: w1fun.renamefun(self.oldNamelist, self.newNamelist, 1, self.Text1)
        #  ************    set the write txt flag and rename flag   **********************
        self.CB1 = tk.Checkbutton(text=_("Process files in subfolders "), variable=CheckVar1, onvalue=1, offvalue=0,
                                  anchor='w', height=1, width=18) # ,background='white',activeforeground='blue'
        self.CB1["command"] = lambda: self.checkinfo(CheckVar1)
        self.CB1.place(x=550, y=135,width=200, height=20)

        self.CB2 = tk.Checkbutton(text=_("Output files"), variable=CheckVar2, onvalue=1, offvalue=0,
                                  anchor='w', height=1, width=18)  # 是否保存文件
        self.CB2.place(x=550, y=155)

        self.CB3 = tk.Checkbutton(text=_("Rename"), variable=CheckVar3, onvalue=1, offvalue=0,
                                  anchor='w', height=1, width=18)

        self.CB3.place(x=550, y=175)
        self.CBindex1 = tk.Checkbutton(text=".srt     ", variable=CheckVar_index1, onvalue=1, offvalue=0,
                                       height=1, width=12)
        self.CBindex1.place(x=50, y=165)
        self.CBindex2 = tk.Checkbutton(text=".eng.srt  ", variable=CheckVar_index2, onvalue=1, offvalue=0,
                            height=1, width=12)
        self.CBindex2.place(x=140, y=165)
        self.CBindex3 = tk.Checkbutton(text=".英文.srt ", variable=CheckVar_index3, onvalue=1, offvalue=0,
                            height=1, width=12)
        self.CBindex3.place(x=230, y=165)
        self.CBindex4 = tk.Checkbutton(text=".简体&英文.srt", variable=CheckVar_index4, onvalue=1, offvalue=0,
                            height=1, width=12)
        self.CBindex4.place(x=70, y=190)
        self.CBindex5 = tk.Checkbutton(text=".繁体&英文.srt", variable=CheckVar_index5, onvalue=1, offvalue=0,
                            height=1, width=13)
        self.CBindex5.place(x=200, y=190)
        self.CBindex6 = tk.Checkbutton(text=".英文.ass", variable=CheckVar_index6, onvalue=1, offvalue=0,
                                       height=1, width=13)
        # self.CBindex6.place(x=220, y=190)
        self.M1=Menu(root)

        self.New_B1=tk.Button(window, text=_("New"))
        self.New_B1.place(x=650, y=260)
        self.New_B1["command"] = self.new_window

        self.B6 = tk.Button(window, text=_("Show information list"))
        self.B6.place(x=630, y=450,width=160, height=30)
        self.B6["command"] = lambda: self.final_printinfo(self.Text1, self.fileselect_sum,self.wordnumberRanksum,
                                                          self.rateRanksum, self.newnameRanksum, self.timecostRanksum)
        self.B6_1 = tk.Button(window, text=_("Clear information list"))
        self.B6_1.place(x=630, y=500,width=160, height=30)
        self.B6_1["command"] = lambda :self.clearinfo(self.Text1)
        self.B6_5 = tk.Button(window, text=_("Show the selected option"))
        self.B6_5.place(x=620, y=300)
        self.B6_5["command"] = lambda: self.printinfo(self.E1.get(), self.E2.get(), CheckVar1.get(), CheckVar2.get(),
                                                      CheckVar3.get(),CheckVar_index1.get(),CheckVar_index2.get(),
                                                      CheckVar_index3.get(),CheckVar_index4.get(),CheckVar_index5.get(),
                                                      CheckVar_index6.get())
        self.B7 = tk.Button(window, text=_("Start"), background='yellow')
        self.B7.configure(font=myFont11)
        self.B7.place(x=670, y=370, height=40, width=60)

        # filepath, indexset2, savetxtflag, txtpath, renameflag, pro_subfileflag
        self.B7["command"] = lambda: self.startrun(self.E1.get(), self.E3.get(), CheckVar2.get(),self.E2.get(),
                                                   CheckVar3.get(), CheckVar1.get(), self.Text1)

    def new_window(self):
        count = 0
        id = _("Are you sure to quit ?") % count
        window = tk.Toplevel(self)
        window.geometry('500x90')
        window.geometry("500x300+600+300")
        label = tk.Label(window, text=id)
        label.pack(side="top", fill="both", padx=10, pady=10)
        B1 = tk.Button(window, text=_("Browse"), command=selectPath).place(x=160, y=50)
        Bquit = tk.Button(window, text=_("Quit！"))
        Bquit.place(x=540, y=140,width=80, height=30)
        Bquit["command"] = root.destroy

    def quitfun(self):
        a = tk.messagebox.askokcancel('Attention', _('Are you sure to quit？'))
        if a:
            window.destroy()

    def startIN (self,filepath):
        if filepath:
            print('The file path is:\n {}'.format(filepath))
        else:
            print('The path should not be empty !')

    def printinfo(self,a,b,c,d,e,*args):
        print('------------------print info------------------------')
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(args)
        print('--------------------------------------------------')

    def checkinfo(self, CheckVar):   # 选中事件
        if CheckVar.get() == 1:      # 判断是否被选中
            CheckVar.set(1)
        else:
            CheckVar.set(0)

    def clearinfo(self, Text):
        Text.configure(state='normal')
        self.Text1.delete('1.0', 'end')
        Text.configure(state='disabled')

    def final_printinfo(self, Text,fileselect_sum, wordnumberRanksum, rateRanksum, newnameRanksum,timecostRanksum):
        Text.configure(state='normal')
        if len(fileselect_sum)==0:
            Text.insert('end', _('No list information currently ！\n'), 'tag_chocolate')

        try:
            if len(wordnumberRanksum)>0:
                Text.insert('end', '='*100+'\n')
                Text.insert('end', _('* Output:  new file name | Word number in total | Total time of the subtitle | Word number per minute')+ '\n','tag_B')
            for i in range(len(wordnumberRanksum)):
                Text.insert('end', newnameRanksum[i] + '\n', 'tag_DarkCyan')
                Text.insert('end', _('Word number in total:')+'{}'.format(wordnumberRanksum[i]) + ' |  ','tag_G')
                Text.insert('end', _('Total time of the subtitle(min):') + ('%.2f minutes' % timecostRanksum[i]) + ' |  ', 'tag_G')
                Text.insert('end', _('Word number per minute:') + str(rateRanksum[i]) + '\n', 'tag_G')
        except Exception as eprint:
            eprint_detail = traceback.format_exc()
            Text.insert('end', _(' Print information  error !\n'), 'tag_Tomato')
            Text.insert('end', '{}\n'.format(eprint), 'tag_Tomato')
            Text.insert('end', '{}\n'.format(eprint_detail), 'tag_Tomato')
        Text.configure(state='disabled')

    def startrun(self, filepath, indexfromText, savetxtflag, txtpath ,renameflag,pro_subfileflag,Text_opreator):
        starttime = time.time()
        Text_opreator.configure(state='normal')
        self.Text1.configure(state='normal')
        listresult=conbine2list(indexfromText, CheckVar_index1.get(), CheckVar_index2.get(), CheckVar_index3.get(),
                                CheckVar_index4.get(), CheckVar_index5.get(), CheckVar_index6.get())
        allflag=1
        try:
            if not filepath:
                allflag = 0
                print('文件路径不能为空 !')
                self.Text1.insert('end', _('The file paths should not be empty !\n'), "tag_Tomato")
            else:
                allflag = 1
            if savetxtflag:
                if not txtpath:
                    allflag = 0
                    print('输出文档路径不能为空 !')
                    self.Text1.insert('end', _('The path of output files should not be empty !\n'), "tag_Tomato")
                else:
                    allflag = 1
            # print(listresult)
            if listresult==None:
                listresult=['.eng.srt']
                print(_('Use the default extension : '), listresult[0])
                self.Text1.insert('end', _('Use the default extension : {}\n').format(listresult[0]), "tag_chocolate")
            if allflag:
                fileselect_sum, wordnumber_sum, subtitlerate_sum, runtime, oldNamelist, newNamelist, \
                newnameRanksum,  oldnameRanksum, rateRanksum, timecostRanksum,wordnumberRanksum= \
                    w1fun.work1_fun_conbine(filepath, listresult, savetxtflag,txtpath, renameflag, pro_subfileflag, Text_opreator)
                self.fileselect_sum = fileselect_sum
                self.wordnumber_sum = wordnumber_sum

                self.oldNamelist = oldNamelist
                self.newNamelist = newNamelist
                print(oldnameRanksum, rateRanksum, timecostRanksum, wordnumberRanksum)
                self.timecostRanksum=timecostRanksum
                self.newnameRanksum=newnameRanksum
                self.oldnameRanksum=oldnameRanksum
                self.rateRanksum=rateRanksum
                self.wordnumberRanksum=wordnumberRanksum
                print(self.newnameRanksum)
                Text_opreator.configure(state='normal')
                self.Text1.configure(state='normal')
                if len(fileselect_sum) > 0:
                    Text_opreator.insert('end', _('* The files are sorted as follows :\n'), 'tag_B')
                for i in range(len(fileselect_sum)):
                    Text_opreator.insert('end', self.newnameRanksum[i]+'\n', 'tag_DarkCyan')
                endtime = time.time()
                runtime=endtime -starttime
                Text_opreator.insert('end', _('>> The running time is {:.3f} s ').format(runtime) + '\n', 'tag_B')
        except Exception as Error1:
            print('Error !')
            error_detail = traceback.format_exc()
            self.Text1.insert('end', _('* System error ! \n'), "tag_R")
            self.Text1.insert('end', '* {} \n'.format(Error1), "tag_R")
            self.Text1.insert('end', '{} \n'.format(error_detail), "tag_R")
            self.Text1.insert('end', _('================================  This is the dividing line   ============================= \n'), "tag_R")

            print('---------------------------')
            print(Error1)
            print(traceback.format_exc())
            print('---------------------------')
        self.Text1.configure(state='disabled')
        Text_opreator.configure(state='disabled')
        print('----   startrun  fun  end    --')


root = window
app = Application(master=root)
app.mainloop()






