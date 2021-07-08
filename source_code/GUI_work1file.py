import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import work1_fun as w1fun
from tkinter.font import Font
import traceback
import tkinter.messagebox
import time
import gettext
import pickle
import threading


def select_path(path_in):
    path_ = askdirectory()
    path_in.set(path_)


def combine_2list(c0, c1, c2, c3, c4, c5, c6):
    listresult = []
    if c0:
        listresult.append(c0)
    if c1:
        listresult.append('.srt')
    if c2:
        listresult.append(".eng.srt")
    if c3:
        listresult.append('.英文.srt')
    if c4:
        listresult.append('.简体&英文.srt')
    if c5:
        listresult.append('.繁体&英文.srt')
    if c6:
        listresult.append('英文.ass')
    return listresult


def save_variable(v, filename):
    f = open(filename, 'wb')
    pickle.dump(v, f)
    f.close()
    return filename


def load_variable(filename):
    f = open(filename, 'rb')
    pickleload = pickle.load(f)
    f.close()
    return pickleload


# global language_option
# language_option=0

def empty(menubar):
    """define the menu language"""
    empty_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label=MENU_empty_Items[-1], menu=empty_menu)


def menu_help(menubar, Text_opreator):
    """define the menu language"""
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(
        label=Help_ITEMS[0],
        command=lambda: help_help(Text_opreator))
    # help_menu.add_separator()
    help_menu.add_command(
        label=Help_ITEMS[1],
        command=lambda: help_version(Text_opreator))
    menubar.add_cascade(label=Help_ITEMS[-1], menu=help_menu)


def help_help(Text_opreator):
    version_info = 'If you have any question,you can refer to http://www.baidu.com or http://www.google.com\n' \
        'You can also call at 123-456789 or send mails to our mailbox: 987654321.163.com.\n' \
        'If you have any other difficulties in using our products,\nyou can contact us via QQ:66666666 ' \
        'or Twitter:@fakeDonaldTrump.\n' \
        'Please look forward to the next version.\nGood luck!\n\nTips: If the wordnumber is 0 , timecost ' \
        'is 1, the rate is 1,there may be something wrong during the processing.\nBe careful to the warming ' \
        'in the information box !'

    Text_opreator.configure(state='normal')
    Text_opreator.insert('end', '=' * 35 + ' Help ' + '=' * 70 + '\n')
    Text_opreator.insert('end', version_info + '\n', "tag_SaddleBrown")
    Text_opreator.insert('end', '=' * 111 + '\n')
    Text_opreator.configure(state='disabled')
    pass


def help_version(Text_opreator):
    versioninfo = 'Product:  Subtitle Words Calculator\n' \
        'Author:   Zhou WB\n' \
        'Date:     2021-03\n' \
        'Version:  1.1\n' \
        'Region:   Xiamen Fujian China\n' \
        'Copyright (c) 2021.\n' \
        'All right reserved.'

    Text_opreator.configure(state='normal')
    Text_opreator.insert('end', '=' * 35 + ' About ' + '=' * 70 + '\n')
    Text_opreator.insert('end', versioninfo + '\n', "tag_SaddleBrown")
    Text_opreator.insert('end', '=' * 111 + '\n')
    Text_opreator.configure(state='disabled')
    pass


def get_menu(tk):
    return Menu(tk)


def init_menu_bar(menubar, file_name_pickle, Text_opreator):
    """initial the menu bar"""
    menu_language(menubar, file_name_pickle)
    menu_help(menubar, Text_opreator)


def menu_language(menubar, file_name_pickle):
    """ define the menu language"""
    sub_language_menu = Menu(menubar, tearoff=0)
    sub_language_menu.add_command(
        label=language_ITEMS[0],
        command=lambda: language_change(file_name_pickle))
    menubar.add_cascade(label=language_ITEMS[-1], menu=sub_language_menu)


def language_change(file_name_pickle):
    """ change the language set_flag """
    try:
        setflag = 1
        option_temp = 0
        save_variable([setflag, option_temp], file_name_pickle)
        winlanguagechange = tk.Tk()
        winlanguagechange.title(_('Attention'))
        winlanguagechange.iconbitmap(".\\icon\\dog.ico")
        winlanguagechange.geometry("360x220+560+280")
        winlanguagechange.maxsize(360, 220)
        winlanguagechange.minsize(360, 220)
        label1 = tk.Label(winlanguagechange, text=(_('You can restart now and select the language !')))
        label1.place(x=20, y=45, width=360, height=80)
        BOK = tk.Button(winlanguagechange, text=(_('OK')))
        BOK.place(x=140, y=140, width=76, height=38)
        BOK["command"] = lambda: winlanguagechange.destroy()

    except Exception as ep:
        print(ep)
    pass


class Work1Calculate(tk.Frame):
    """the main GUI class """
    count = 0
    option = 1

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        # option = 2
        # print(option)
        # selectLanguage(option)  the language of function inside the Class
        # would be changed

    def createWidgets(self):
        #  all kinds of label

        self.master.title(
            _("       Count the number of words per minute in the subtitle file and generate a text file      "))
        self.canvas1 = tk.Canvas(window, width=360, height=110)
        self.canvas1.place(x=510, y=108)
        self.canvas1.create_rectangle(10, 4, 275, 100, outline='gray')
        self.canvas2 = tk.Canvas(window, width=560, height=20)  # bg='pink'
        self.canvas2.place(x=27, y=250)
        self.canvas2.create_rectangle(0, 13, 560, 13.1, fill='gray')
        self.L1 = tk.Label(window, text=_('Object path:'))
        self.L1.place(x=12, y=20, width=80, height=30)
        self.L5 = tk.Label(window, text='350,150')
        # self.L5.place(x=350, y=150, width=80, height=30)
        self.L2 = tk.Label(window, text=_('Output \npath:'))
        self.L2.place(x=12, y=72, width=80, height=30)
        self.L3 = tk.Label(window, text=_('Customize \nextension:'))
        self.L3.place(x=12, y=124, width=80, height=30)
        # self.L4 = tk.Label(window, text='by Zhou WB\n@2021/03 \nVersion:1.0 ')
        # self.L4.place(x=660, y=540)
        # file path selection and output path selection
        self.L5 = tk.Label(window, text=_('  Information  '))
        self.L5.place(x=285, y=250)
        self.L6 = tk.Label(window, text=_('Option:'))  # , bg='blue'
        self.L6.place(x=530, y=115, width=100, height=20)
        self.E1 = tk.Entry(window, textvariable=path, highlightcolor='blue')
        self.E1.place(x=105, y=15, width=575, height=30)

        self.BE1 = tk.Button(window,text=_("Browse"),
            command=lambda: select_path(path),background='white')
        self.BE1.place(x=715, y=14, width=80, height=30)
        self.E2 = tk.Entry(window, textvariable=path2, highlightcolor='blue')
        self.E2.place(x=105, y=70, width=575, height=30)
        self.BE2 = tk.Button(window,text=_("Browse"),command=lambda: select_path(path2),background='white')
        self.BE2.place(x=715, y=70, width=80, height=30)
        # about extension
        self.E3 = tk.Entry(window,textvariable=extension1,highlightcolor='blue')
        self.E3.place(x=105, y=125, width=210, height=30)
        # to show info
        # self.E4 = tk.Entry(window, textvariable=info_show, highlightcolor='white')
        # self.E4.place(x=80, y=350, width=400, height=60)
        txtwidth = 560
        txtheight = 320
        txt_x = 30
        txt_y = 280
        self.Text1 = tk.Text(window, wrap='none')
        self.Text1.place(width=txtwidth, height=txtheight, x=txt_x, y=txt_y)
        self.Text1.configure(state='disabled')
        self.Text1.see(END)
        scroll_y = tk.Scrollbar()
        scroll_y.place(width=20, height=txtheight, x=txt_x + txtwidth + 2, y=txt_y)
        scroll_x = tk.Scrollbar(window, orient='horizontal')
        scroll_x.place(width=txtwidth, height=20, x=txt_x, y=txt_y + txtheight +2)
        self.fileselect_sum = []
        self.wordnumber_sum = []
        self.subtitlerate_sum = []
        self.oldNamelist = []
        self.newNamelist = []
        self.newNameaddlist = []
        self.timecostsum = []
        self.timecostRanksum = []
        self.newnameRanksum = []
        self.oldnameRanksum = []
        self.rateRanksum = []
        self.wordnumberRanksum = []
        # connect
        scroll_y.config(command=self.Text1.yview)
        scroll_x.config(command=self.Text1.xview)
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
        self.Text1.tag_config("tag_DarkCyan", foreground="DarkCyan")
        self.Text1.tag_config("tag_Tomato", foreground="Tomato")
        self.Text1.tag_config("tag_SaddleBrown", foreground="SaddleBrown")
        my_font = Font(size=10)
        # my_font11 = Font(size=11)
        my_font12 = Font(family="微软雅黑", size=12)
        # my_font = Font(family="Arial", size=12)
        self.Text1.configure(font=my_font)
        self.B2 = tk.Button(window, text=_("Quit"))
        self.B2.place(x=670, y=545, width=80, height=30)
        self.B2["command"] = lambda: self.quit_fun()
        self.B3 = tk.Button(window, text=_("Start"), background='blue')
        self.B3["command"] = lambda: self.startIN(self.E1.get())
        # # self.B3.place(x=450, y=210)
        self.B5_recover = tk.Button(window,text=_("Recover"),highlightcolor='white', width=9, height=1)
        self.B5_recover.place(x=670, y=218, width=100, height=30)
        self.B5_recover["command"] = lambda: w1fun.rename_fun(
            self.oldNamelist, self.newNamelist, -1, self.Text1)
        self.B5rename = tk.Button(window, text=_("Rename"), highlightcolor='white', width=9, height=1)
        self.B5rename.place(x=550, y=218, width=100, height=30)
        self.B5rename["command"] = lambda: w1fun.rename_fun(
            self.oldNamelist, self.newNamelist, 1, self.Text1)
        #  ************    set the write txt flag and rename flag   ***********
        self.CB1 = tk.Checkbutton(text=_("Process files in subfolders "), variable=check_var1, onvalue=1, offvalue=0,
                                  anchor='w', height=1, width=18)  # ,background='white',activeforeground='blue'
        self.CB1["command"] = lambda: self.checkinfo(check_var1)
        self.CB1.place(x=550, y=135, width=200, height=20)

        self.CB2 = tk.Checkbutton(text=_("Output files"), variable=check_var2, onvalue=1, offvalue=0,
                                  anchor='w', height=1, width=18)  # whether to save file
        self.CB2.place(x=550, y=155)

        self.CB3 = tk.Checkbutton(text=_("Rename"), variable=check_var3, onvalue=1, offvalue=0,
                                  anchor='w', height=1, width=18)
        self.CB3.place(x=550, y=175)
        self.CBindex1 = tk.Checkbutton(text=".srt     ", variable=check_var_index1, onvalue=1, offvalue=0,
                                       height=1, width=12)
        self.CBindex1.place(x=50, y=165)
        self.CBindex2 = tk.Checkbutton(text=".eng.srt  ", variable=check_var_index2, onvalue=1, offvalue=0,
                                       height=1, width=12)
        self.CBindex2.place(x=140, y=165)
        self.CBindex3 = tk.Checkbutton(text=".英文.srt ", variable=check_var_index3, onvalue=1, offvalue=0,
                                       height=1, width=12)
        self.CBindex3.place(x=230, y=165)
        self.CBindex4 = tk.Checkbutton(text=".简体&英文.srt", variable=check_var_index4, onvalue=1, offvalue=0,
                                       height=1, width=12)
        self.CBindex4.place(x=70, y=190)
        self.CBindex5 = tk.Checkbutton(text=".繁体&英文.srt", variable=check_var_index5, onvalue=1, offvalue=0,
                                       height=1, width=13)
        self.CBindex5.place(x=200, y=190)
        self.CBindex6 = tk.Checkbutton(text=".英文.ass", variable=check_var_index6, onvalue=1, offvalue=0,
                                       height=1, width=13)
        # self.CBindex6.place(x=220, y=190)
        self.M1 = Menu(root)
        menubar = get_menu(root)
        init_menu_bar(menubar, file_name_pickle, self.Text1)
        root.config(menu=menubar)

        self.New_B1 = tk.Button(window, text=_("New"))
        # self.New_B1.place(x=650, y=260)
        self.New_B1["command"] = self.new_window

        self.B6 = tk.Button(window, text=_("Show information list"))
        self.B6.place(x=630, y=430, width=180, height=30)
        self.B6["command"] = lambda: self.final_printinfo(self.Text1, self.fileselect_sum, self.wordnumberRanksum,
                                                          self.rateRanksum, self.newnameRanksum, self.timecostRanksum)
        self.B6_1 = tk.Button(window, text=_("Clear information list"))
        self.B6_1.place(x=630, y=480, width=180, height=30)
        self.B6_1["command"] = lambda: self.clear_info(self.Text1)
        self.B6_5 = tk.Button(window, text=_("Show the selected option"))
        # self.B6_5.place(x=650, y=300)
        self.B6_5["command"] = lambda: self.printinfo(self.E1.get(), self.E2.get(), check_var1.get(), check_var2.get(),
                                                      check_var3.get(), check_var_index1.get(), check_var_index2.get(),
                                                      check_var_index3.get(), check_var_index4.get(),
                                                      check_var_index5.get(),
                                                      check_var_index6.get())
        self.B7 = tk.Button(window, text=_("Start"), background='yellow')
        self.B7.configure(font=my_font12)
        self.B7.place(x=680, y=340, height=45, width=65)

        # filepath, indexset2, savetxtflag, txtpath, renameflag, pro_subfileflag
        self.B7["command"] = lambda: self.startrun(self.E1.get(), self.E3.get(), check_var2.get(), self.E2.get(),
                                                   check_var3.get(), check_var1.get(), self.Text1)

    def new_window(self):  # for test
        count = 0
        id = _("Are you sure to quit ?") % count
        window = tk.Toplevel(self)
        window.geometry('500x90')
        window.geometry("500x300+600+300")
        label = tk.Label(window, text=id)
        label.pack(side="top", fill="both", padx=10, pady=10)
        B1 = tk.Button(window,text=_("Browse"),command=select_path(path)).place(x=160, y=50)
        Bquit = tk.Button(window, text=_("Quit！"))
        Bquit.place(x=540, y=140, width=80, height=30)
        Bquit["command"] = root.destroy

    def quit_fun(self):
        quit_confirm = tk.messagebox.askokcancel(_('Attention'), _('Are you sure to quit ? '))
        if quit_confirm:
            window.destroy()

    def startIN(self, filepath):   # for test
        if filepath:
            pass
            # print('The file path is:\n {}'.format(filepath))
        else:
            pass
            # print('The path should not be empty !')

    def printinfo(self, a, b, c, d, e, *args):
        pass
        print('------------------print info------------------------')
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(args)
        print('--------------------------------------------------')

    def checkinfo(self, CheckVar):
        if CheckVar.get() == 1:
            CheckVar.set(1)
        else:
            CheckVar.set(0)

    def clear_info(self, text):
        text.configure(state='normal')
        self.Text1.delete('1.0', 'end')
        text.configure(state='disabled')

    def final_printinfo(self, Text, fileselect_sum, wordnumberRanksum,
                        rateRanksum, newnameRanksum, timecostRanksum):

        def thread_printinfo(Text, fileselect_sum, wordnumberRanksum,
                             rateRanksum, newnameRanksum, timecostRanksum):
            Text.configure(state='normal')
            if len(fileselect_sum) == 0:

                Text.insert('end',_('No list information currently ！\n'),'tag_chocolate')
                Text.configure(state='disabled')

            try:
                if len(wordnumberRanksum) > 0:
                    Text.configure(state='normal')
                    Text.insert('end', '=' * 110 + '\n')
                    Text.insert('end', _(
                        '* Output:  new file name | Word number in total | Total time of the subtitle | Word number per minute') + '\n',
                        'tag_B')
                    Text.configure(state='disabled')
                for i in range(len(wordnumberRanksum)):
                    Text.configure(state='normal')
                    Text.insert('end',newnameRanksum[i] + '\n', 'tag_DarkCyan')
                    Text.insert('end',_('Word number in total:') +'{}'.format(wordnumberRanksum[i]) +' | ', 'tag_G')
                    Text.insert('end', _('Total time of the subtitle(min):') + ('%.2f' % timecostRanksum[i]) + ' | ',
                                'tag_G')
                    Text.insert('end', _('Word number per minute:') +str(rateRanksum[i]), 'tag_G')
                    Text.insert('end', '      \n', 'tag_G')
                    Text.see('end')
                    Text.configure(state='disabled')
            except Exception as eprint:
                eprint_detail = traceback.format_exc()
                Text.configure(state='normal')
                Text.insert('end',_(' Print information  error !\n'),'tag_Tomato')
                Text.insert('end', '{}\n'.format(eprint), 'tag_Tomato')
                Text.insert('end', '{}\n'.format(eprint_detail), 'tag_Tomato')
                Text.configure(state='disabled')

        th_print_info = threading.Thread(target=thread_printinfo, args=(Text, fileselect_sum, wordnumberRanksum,
                                                                        rateRanksum, newnameRanksum, timecostRanksum))
        th_print_info.setDaemon(True)
        th_print_info.start()

    def startrun(self, filepath, indexfromText, savetxtflag,
                 txtpath, renameflag, pro_subfileflag, Text_opreator):

        def processfun(filepath, indexfromText, savetxtflag,
                       txtpath, renameflag, pro_subfileflag, Text_opreator):
            starttime = time.time()
            Text_opreator.configure(state='normal')
            self.Text1.configure(state='normal')
            listresult = combine_2list(indexfromText, check_var_index1.get(), check_var_index2.get(),
                                       check_var_index3.get(),
                                       check_var_index4.get(), check_var_index5.get(), check_var_index6.get())
            allflag = 1
            try:
                if not filepath:
                    allflag = 0
                    print('The file path cannot be empty !')
                    self.Text1.insert(
                        'end', _('The file path cannot be empty !\n'), "tag_Tomato")
                else:
                    allflag = 1
                if savetxtflag:
                    if not txtpath:
                        allflag = 0
                        print('The path of output files should not be empty !')
                        self.Text1.insert(
                            'end', _('The path of output files should not be empty !\n'), "tag_Tomato")
                    else:
                        allflag = 1
                # print(listresult)
                if listresult is None:
                    listresult = ['.eng.srt']
                    print(_('Use the default extension : '), listresult[0])
                    self.Text1.insert('end', _('Use the default extension : {}\n').format(listresult[0]),
                                      "tag_chocolate")
                if allflag:
                    fileselect_sum, wordnumber_sum, subtitlerate_sum, runtime, oldNamelist, newNamelist, \
                        newnameRanksum, oldnameRanksum, rateRanksum, timecostRanksum, wordnumberRanksum = \
                        w1fun.work1_fun_conbine(filepath, listresult, savetxtflag, txtpath, renameflag, pro_subfileflag,
                                                Text_opreator)

                    self.fileselect_sum = fileselect_sum
                    self.wordnumber_sum = wordnumber_sum

                    self.oldNamelist = oldNamelist
                    self.newNamelist = newNamelist
                    # print('the oldnameRanksum, rateRanksum, timecostRanksum, wordnumberRanksum ')
                    # print(len(oldnameRanksum), len(rateRanksum), len(timecostRanksum), len(wordnumberRanksum))
                    self.timecostRanksum = timecostRanksum
                    self.newnameRanksum = newnameRanksum
                    self.oldnameRanksum = oldnameRanksum
                    self.rateRanksum = rateRanksum
                    self.wordnumberRanksum = wordnumberRanksum
                    # print(self.newnameRanksum)
                    Text_opreator.configure(state='normal')
                    self.Text1.configure(state='normal')
                    if len(fileselect_sum) > 0:
                        Text_opreator.insert('end', '-' * 110 + '\n')
                        Text_opreator.insert('end', _('* The files are sorted as follows :\n'), 'tag_B')
                    for i in range(len(fileselect_sum)):
                        Text_opreator.insert(
                            'end', self.newnameRanksum[i] + '\n', 'tag_DarkCyan')
                    endtime = time.time()
                    runtime = endtime - starttime
                    Text_opreator.insert('end', _('>> The running time is {:.3f} s ').format(runtime) + '\n', 'tag_B')
            except Exception as Error1:
                print('Error !')
                error_detail = traceback.format_exc()
                self.Text1.insert('end', _('* System error ! \n'), "tag_R")
                self.Text1.insert('end', '* {} \n'.format(Error1), "tag_R")
                self.Text1.insert('end', '{} \n'.format(error_detail), "tag_R")
                self.Text1.insert('end', _(
                    '================================  This is the dividing line   ============================= \n'),
                    "tag_R")

                print('---------------------------')
                print(Error1)
                print(traceback.format_exc())
                print('---------------------------')
            self.Text1.configure(state='disabled')
            Text_opreator.configure(state='disabled')
            print('----   startrun  fun  end    --')
            pass

        thread_start = threading.Thread(target=processfun,
                                        args=(filepath, indexfromText, savetxtflag, txtpath, renameflag,
                                              pro_subfileflag, Text_opreator))
        thread_start.setDaemon(True)
        thread_start.start()


global language_option
# language_option = 0


class theMessageBox():
    def __init__(self, content=[]):
        self.content = content
        # content would be    0 title ,1 question, 2language
        self.window = tk.Tk()
        # 1 need to reselect  0 don't need to select
        self.CheckFlag = IntVar(self.window)
        self.title1 = self.content[0]
        self.Text1 = self.content[1]
        self.Button_yes = tk.Button(self.window, text=self.yesfun(
            self.content[2]), command=lambda: self.changeflag(0))
        self.Button_yes.place(x=203, y=203)  # , background='white'
        self.Button_no = tk.Button(self.window, text=self.nofun(
            self.content[2]), command=lambda: self.changeflag(1))
        self.Button_no.place(x=203, y=203)
        self.window.mainloop()

    def yesfun(self, language):
        if language == 'English':
            return 'Yes'
        elif language == 'Chinese':
            return '是'
        elif language == 'French':
            return 'Oui'
        elif language == 'Japanese':
            return 'はい'
        else:
            return '??'
        pass

    def nofun(self, language):
        if language == 'English':
            return 'No'
        elif language == 'Chinese':
            return '否'
        elif language == 'French':
            return 'non'
        elif language == 'Japanese':
            return 'いいえ '
        else:
            return '！！'
        pass

    def changeflag(self, status):
        self.CheckFlag = status
        self.window.destroy()
        pass


class LanguageSelect():
    """ the language select box  """

    def __init__(self):

        self.CheckFlag = 1   # 1 need to reselect  0 don't need to select
        self.languageoption = 0   # default option 0

    def add_somthing(self):
        self.lan_window = tk.Tk()
        self.lan_window.geometry("400x300+600+300")
        self.lan_window.title('    Please select the language    ')
        self.lan_window.minsize(400, 300)
        self.lan_window.maxsize(400, 300)
        try:
            self.lan_window.tk.call('wm', 'iconphoto', self.lan_window._w, tk.PhotoImage(
                    file='.\\icon\\huaji.png'))
        except BaseException:
            pass
        title0 = 'Attention'
        question0 = 'Whether to save this setting ?'
        B0 = tk.Button(self.lan_window, text='English')
        B0.place(x=150, y=50, width=100, height=30)
        B0["command"] = lambda: self.getmessagebox([title0, question0], 0)

        title1 = '注意'
        question1 = '是否保存这个设置 ?'
        B1 = tk.Button(self.lan_window, text="中文")
        B1.place(x=150, y=90, width=100, height=30)
        B1["command"] = lambda: self.getmessagebox([title1, question1], 1)

        title2 = 'Remarque '
        question2 = "S'il faut enregistrer ce paramètre ?"
        B2 = tk.Button(self.lan_window, text='français')
        B2.place(x=150, y=130, width=100, height=30)
        B2["command"] = lambda: self.getmessagebox([title2, question2], 2)

        title3 = '注意'
        question3 = 'この設定を保存するかどうか  ?'
        B3 = tk.Button(self.lan_window, text='日本語')
        B3.place(x=150, y=170, width=100, height=30)
        B3["command"] = lambda: self.getmessagebox([title3, question3], 3)
        self.lan_window.mainloop()

    def getmessagebox(self, content, languagesetnum):
        self.title1 = content[0]
        self.Text1 = content[1]
        self.languageoption = languagesetnum
        self.messagewindow = tk.Toplevel(self.lan_window)
        self.messagewindow.geometry("320x200+650+350")
        self.messagewindow.minsize(320, 200)
        self.messagewindow.maxsize(320, 200)
        try:
            self.messagewindow.tk.call('wm', 'iconphoto', self.messagewindow._w, tk.PhotoImage(
                    file='.\\icon\\dog1.png'))
        except BaseException:
            pass
        self.messagewindow.title(self.title1)
        self.CheckFlag = IntVar()   # 1 need to reselect  0 don't need to select
        self.Label1 = tk.Label(self.messagewindow, text=self.Text1)
        self.Label1.place(x=10, y=40, width=300, height=30)
        self.Buttonyes = tk.Button(self.messagewindow,text=self.yesfun(languagesetnum),command=lambda: self.changeflag(0))
        self.Buttonyes.place(x=65,y=120, width=55, height=35)  # , background='white'
        self.Buttonno = tk.Button( self.messagewindow,text=self.nofun(languagesetnum),command=lambda: self.changeflag(1))
        self.Buttonno.place(x=215, y=120, width=55, height=35)
        self.messagewindow.mainloop()

    def yesfun(self, languagesetnum):
        if languagesetnum == 0:  # English
            return 'Yes'
        elif languagesetnum == 1:  # Chinese
            return '是'
        elif languagesetnum == 2:  # French
            return 'Oui'
        elif languagesetnum == 3:  # Japanese
            return 'はい'
        else:
            return '??'
        pass

    def nofun(self, languagesetnum):
        if languagesetnum == 0:
            return 'No'
        elif languagesetnum == 1:
            return '否'
        elif languagesetnum == 2:
            return 'non'
        elif languagesetnum == 3:
            return 'いいえ '
        else:
            return '！！'
        pass

    def changeflag(self, status):
        # 0 :save the option  1:do not save the option
        self.CheckFlag = status
        self.messagewindow.destroy()
        self.lan_window.destroy()
        pass


# get the default file
file_name_pickle = r'.\locale\Setting.pickle'
try:
    # try to open f[0] for setting flag  f[1] for option
    f = load_variable(file_name_pickle)
    set_flag = f[0]
    language_option = f[1]

except BaseException:

    # if none get a new one initial setting flag=1  option=0
    set_flag = 1  # need to set language
    option_temp = 0  # default option :English
    file = save_variable([set_flag, option_temp], file_name_pickle)
    f = load_variable(file)
    # print('Creat new file')
    # print('f=', f)

if set_flag:
    # print('Here is the set flag ')
    languagebox = LanguageSelect()
    languagebox.add_somthing()
    option_temp = languagebox.languageoption
    set_flag = languagebox.CheckFlag
    # t=input('set_flag ')
    # print('set_flag',set_flag)
    # print('option_temp',option_temp)
    try:
        file = save_variable([set_flag, option_temp], file_name_pickle)
    except BaseException:
        # if choose nothing ,the default language is English
        file = save_variable([1, 0], file_name_pickle)
else:
    f = load_variable(file_name_pickle)
    # set_flag = f[0]
    language_option = f[1]

f = load_variable(file_name_pickle)
language_option = f[1]
# print('language_option=', language_option)

# --------------------------------------------------------------------------------------------
if language_option == 0:
    current_filepath = os.path.dirname(os.path.abspath(__file__))
    language = gettext.translation('en_GUI_Work1', localedir=os.path.join(current_filepath, 'locale'),
                                   languages=['en'])
    language.install()
elif language_option == 1:
    current_filepath = os.path.dirname(os.path.abspath(__file__))
    language = gettext.translation('zh_GUI_work1_combine', localedir=os.path.join(current_filepath, 'locale'),
                                   languages=['zh'])
    language.install()
elif language_option == 2:
    current_filepath = os.path.dirname(os.path.abspath(__file__))
    language = gettext.translation('fr_work1_fun', localedir=os.path.join(current_filepath, 'locale'),
                                   languages=['fr'])
    language.install()
elif language_option == 3:
    current_filepath = os.path.dirname(os.path.abspath(__file__))
    language = gettext.translation(
        'ja', localedir=os.path.join(
            current_filepath, 'locale'), languages=['ja'])
    language.install()
else:
    pass

MENU_empty_Items = [
    '                                                                     ']
language_ITEMS = [_('Reselect language'), _('Language')]
# , '中文', 'français', '日本語', _('other')
Help_ITEMS = [_('See help'), _('About'), _('Help')]

# --------------------------------------------------------------------------

window = tk.Tk()
window.geometry("830x650+400+100")
try:
    window.tk.call('wm','iconphoto',window._w,tk.PhotoImage(file='.\\icon\\cow.png'))
except BaseException:
    pass
window.minsize(830, 650)
window.maxsize(830, 650)

root = window

path = StringVar()
path2 = StringVar()
extension1 = StringVar()
info_show = StringVar()
check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()
check_var_index1 = IntVar()
check_var_index2 = IntVar()
check_var_index3 = IntVar()
check_var_index4 = IntVar()
check_var_index5 = IntVar()
check_var_index6 = IntVar()

app = Work1Calculate(master=root)


if __name__ == '__main__':
    app.mainloop()
