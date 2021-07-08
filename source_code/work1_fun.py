# Calculate the frequent of the English word
# give a path then process all the file(according to the extension)
"""
projet:  高级编程技术 课程作业一
function:Calculate the frequency of the English words insubtitle
version: 1.1
author:  Zhou WB
time:    2021-03
"""

import os
import re
import time
import chardet
import traceback
import math
import gettext

global filelist_G
global filenamelist_G
global pathlist_G

pathlist_G = []
filenamelist_G = []


def getfile_path(filepath):
    global filenamelist_G
    global pathlist_G
    # search the file on
    files = os.listdir(filepath)   # files can be folders or files
    for fitem in files:
        pathjoin = os.path.join(filepath, fitem)

        # print(Pathjoin)
        if os.path.isdir(pathjoin):
            # print('11111111')
            getfile_path(pathjoin)
        else:
            # print('22222222')
            # print(os.path.join(filepath, pathjoin))
            final_path = os.path.join(filepath, fitem)
            # print('----------------------------')
            # print('join test :',filepath, fitem)
            # print('join result :', final_path)
            # print('----------------------------')

            pathlist_G.append(final_path)
            filenamelist_G.append(fitem)

    return pathlist_G, filenamelist_G


def calculate_word(filepath, *args):
    # the filepath need to be absolute path
    # input a file path  and file extension;
    # output the wordnumber timecost rate;
    if args:
        Text = args[0]
        textinfo = 1
    else:
        textinfo = 0
        Text = []

    patt2 = r'-->'
    pattern2 = re.compile(patt2)
    patt3 = r'(\d*):(\d*):(\d*)[\,\.](\d*)\W*-->\W*(\d*):(\d*):(\d*)[\,\.](\d*)'
    pattern3_time = re.compile(patt3)
    patt4_Englishword = r'[a-z]'
    pattern4_Englishword = re.compile(patt4_Englishword)
    patt5_char = r'{.*}'
    pattern5_char = re.compile(patt5_char)
    # print(check1)

    # print('......... '+'Open the file' +'......... ')
    try:
        # print('------> :', filepath)
        a = filepath.replace('\\', "/", 100)
        # print(a)
        f1 = open(a, 'rb')  #

        data = f1.read()  # get the file name
        encodingformat = chardet.detect(data).get('encoding')  # get the coding format
        # print(encoding_format)
        f1.close()
        with open(filepath, encoding=encodingformat, errors='ignore') as file:
            # reading the word and calculate  # errors set as 'ignore' for
            # enable the normal reading
            flag1 = 0
            i = 0
            wordnumber = 0
            timecost = 0
            rate = 0
            while True:
                lineread = file.readline()
                i = i + 1
                # print('*-------* reading line: {}  *-------*'.format(i))
                # check if the subtitle time line
                result = pattern2.findall(lineread)
                # print(result)
                if result:
                    timeread = pattern3_time.findall(lineread)
                    if timeread:
                        row_starttime_temp = 60 * int(timeread[0][0]) + int(timeread[0][1]) + 1 / 60 * int(
                            timeread[0][2]) + 1 / 60000 * int(timeread[0][3])
                        row_endtime_temp = 60 * int(timeread[0][4]) + int(timeread[0][5]) + 1 / 60 * int(
                            timeread[0][6]) + 1 / 60000 * int(timeread[0][7])
                        delta_time = row_endtime_temp - row_starttime_temp
                        # print('The end time is:{} '.format(endtime[0]))
                        # print('The time cost(in minute)is:%5.4f ' % timecost)
                        flag1 = 1  # it is a time flag
                    else:
                        pass
                    continue
                if flag1:
                    result_char = pattern5_char.findall(lineread)
                    if result_char:        #
                        pass
                    else:
                        result_English = pattern4_Englishword.findall(lineread)
                        if result_English:   # if the line is English
                            temp_words = lineread.split(None)
                            # for testing
                            # print(('temp_words is %s ,and the length is %d') % (temp_words,len(temp_words)))
                            wordnumber = wordnumber + len(temp_words)
                            timecost = timecost + delta_time
                            if len(temp_words) == 0:
                                flag1 = 0
                            pass
                # print(lineread)
                if not lineread:
                    break
                pass
            # timecost=0  # for test error
            try:
                rate = math.floor(wordnumber / timecost)
            except BaseException:
                rate = 0
                pass
            # check data
            # print(('The number of line is:               {}').format(i))
            # print(('The number of the word is:           {}').format(wordnumber))
            # print(('The end time is:                     {}:{}:{}:{} ').format(timeread[0][4], timeread[0][5],
            #                                                                  timeread[0][6], timeread[0][7]))
            # print(('The total time of the subtitle is:   {:.3f} minutes ').format(timecost))
            # print(('Word per minute is:                  {}').format(rate))
        success_flag = 1
    except Exception as e_op:
        error_detail = traceback.format_exc()
        success_flag = 0
        wordnumber = 0
        timecost = 1
        rate = 1
        if textinfo:
            Text.insert('end','Open file error!\n{} ! \n'.format(e_op),"tag_R")
            Text.insert('end', '{} \n'.format(error_detail), "tag_R")
            Text.see('end')

    return wordnumber, timecost, rate, success_flag


def rename_fun(oldNamelist, newNamelist, flag, *args):
    # flag == 0 do nothing
    if args:
        Text = args[0]
        textinfo = 1
        Text.configure(state='normal')
    else:
        textinfo = 0
        Text = []
    t = 0
    if textinfo:
        if flag == 1:
            Text.insert('end', '-' * 110 + '\n')
            Text.insert('end', _('{} files need to be renamed  !\n').format(len(oldNamelist)), "tag_B")
        elif flag == -1:
            Text.insert('end', '-' * 110 + '\n')
            Text.insert('end', _('{} files need to be recovered !\n').format(len(oldNamelist)), "tag_B")
        else:
            pass
    for i in range(len(oldNamelist)):
        try:
            if flag == 1:
                os.rename(oldNamelist[i], newNamelist[i])
                if textinfo:
                    Text.insert('end', newNamelist[i] + '\n', 'tag_DarkCyan')
                t = t + 1
            elif flag == -1:
                os.rename(newNamelist[i], oldNamelist[i])
                if textinfo:
                    Text.insert('end', oldNamelist[i] + '\n', 'tag_DarkCyan')
                t = t + 1
            else:
                pass
        except Exception as e_rename:
            traceback_rename = traceback.format_exc()
            if flag == 1:
                print('Error when rename !')
                print(e_rename)
                print(traceback_rename)

                if textinfo:
                    Text.insert('end', '*> NO.{} Error when rename !  \n'.format(i), "tag_R")
                    Text.insert('end', '{} ! \n'.format(e_rename), "tag_R")
                    # Text.insert('end', '{}\n'.format(traceback_rename), "tag_R")

            elif flag == -1:
                print('Error when recover !')
                print(e_rename)
                print(traceback_rename)
                if textinfo:
                    Text.insert('end', '*> NO.{} Error when recover !  \n'.format(i), "tag_R")
                    Text.insert('end', '{} ! \n'.format(e_rename), "tag_R")
                    # Text.insert('end', '{}\n'.format(traceback_rename), "tag_R")
            else:
                if textinfo:
                    Text.insert('end', '*> Error when use other flag ! \n', "tag_R")
                    Text.insert('end', '{} ! \n'.format(e_rename), "tag_R")
    if flag == 1:
        print('Rename finished  ! {} files done ! '.format(t))
        if textinfo:
            Text.insert(
                'end',
                _('Rename finished  ! {} files done !\n').format(t),
                "tag_B")
    elif flag == -1:
        print('Recover finished ! {} files done ! '.format(t))
        if textinfo:
            Text.insert(
                'end',
                _('Recover finished  ! {} files done ! \n').format(t),
                "tag_B")
    else:
        print('Not rename ')
        if textinfo:
            Text.insert('end', _('Not rename any file.  \n'), "tag_B")

    if textinfo:
        Text.configure(state='disabled')


def rank_data(rateRankref, fileselect_sum, subtitlerate_sum, wordnumber_sum, timecostsum):
    oldnameRanksum = []
    rateRanksum = []
    timecostRanksum = []
    wordnumberRanksum = []
    for i in range(len(rateRankref)):
        indextemp = rateRankref[i][1][0]
        oldnameRanksum.append(fileselect_sum[indextemp])
        rateRanksum.append(subtitlerate_sum[indextemp])
        timecostRanksum.append(timecostsum[indextemp])
        wordnumberRanksum.append(wordnumber_sum[indextemp])
    return oldnameRanksum, rateRanksum, timecostRanksum, wordnumberRanksum


def get_name(subtitlerate_sum, pathselect_sum, fileselect_sum):
    # get the rank
    rateRank = sorted(enumerate(subtitlerate_sum), key=lambda x: x[1])
    rateRankref = sorted(enumerate(rateRank))
    # print('get the new file name ')
    oldNamelist = []
    newNamelist = []
    newNameRanksum = []
    rateRanksum = []
    for i in range(len(subtitlerate_sum)):
        # print(c[i][1][1])  # rate value
        # for the subtitle rate,the relevant index in the list
        idx = rateRankref[i][1][0]
        ratetemp = subtitlerate_sum[idx]
        oldNamelist.append(pathselect_sum[idx])
        folder_path, file_name = os.path.split(pathselect_sum[idx])
        newNameadd = (('%05d@' % (i + 1)) + fileselect_sum[idx])
        # print('newNameadd is {} '.format(newNameadd))
        newNamelist.append(folder_path + '/' + newNameadd)
        newNameRanksum.append(newNameadd)
        rateRanksum.append(ratetemp)
    return oldNamelist, newNamelist, newNameRanksum, rateRankref


def write_txt(txtpath, writeflag, SubtitleRateSum, rateRanksort, FilenameSum):
    if SubtitleRateSum:
        time0 = time.localtime(time.time())
        name_default1 = 'doc1_' + str(time0.tm_hour) + '_' + str(time0.tm_min) + \
            '_' + str(time0.tm_sec) + '.txt'
        name_default2 = 'doc2_' + str(time0.tm_hour) + '_' + str(time0.tm_min) + \
            '_' + str(time0.tm_sec) + '.txt'
        path1 = txtpath + '/' + name_default1
        path2 = txtpath + '/' + name_default2
        # print(path1)
        if writeflag:
            with open(path1, 'w+')as f:
                oldNamelist = []
                newNamelist = []
                for i in range(len(SubtitleRateSum)):
                    # for the subtitle rate,the relevant index in the list
                    idx = rateRanksort[i][1][0]
                    ratetemp = SubtitleRateSum[idx]
                    # print('NO.{}'.format(i+1))
                    # print('the rate is:  {}'.format(rateRanksort[i][1][1]))
                    # print('the origin filename is:  {}'.format(FilenameSum[idx]))
                    f.write(('%05d@' %(i + 1)) + FilenameSum[idx] + '____' + ('%.0f' %ratetemp) + '\n')
            with open(path2, 'w+')as f:
                oldNamelist = []
                newNamelist = []
                for i in range(len(SubtitleRateSum)):
                    # for the subtitle rate,the relevant index in the list
                    idx = rateRanksort[i][1][0]
                    ratetemp = SubtitleRateSum[idx]
                    # print('NO.{}'.format(i+1))
                    # print('the rate is:  {}'.format(rateRanksort[i][1][1]))
                    # print('the origin filename is:  {}'.format(FilenameSum[idx]))
                    f.write(FilenameSum[idx] + '____' +('%.0f' % ratetemp) + '\n')


def work1_fun_conbine(filepath, indexset, savetxtflag,txtpath, renameflag, pro_subfileflag, *args):
    global filenamelist_G
    global pathlist_G
    # print('filepath read is ',filepath )
    fileselect_sum = []        # save the fileselect_sum     we select
    wordnumber_sum = []        # save the wordnumber_sum     we select
    subtitlerate_sum = []      # save the subtitlerate_sum   we select
    pathselect_sum = []        # save the pathselect_sum     we select
    timecostsum = []
    start = time.time()
    if args:
        Text = args[0]
        textinfo = 1
    else:
        textinfo = 0
        Text = []
    # print('pro_subfileflag :', pro_subfileflag)
    # print(type(pro_subfileflag))
    if pro_subfileflag == 1:
        # print('Searching all files ...... ')
        if textinfo:
            Text.configure(state='normal')
            Text.insert('end', '-' * 110 + '\n')
            Text.insert('end', _('* Searching all files ...... \n'), "tag_purple")
            Text.configure(state='disabled')
        pathlist_G = []      # reset the global variable in the getfile_path function
        filenamelist_G = []
        pathlist, filenamelist = getfile_path(filepath)
        pathlist_G = []  # reset the global variable in the getfile_path function
        filenamelist_G = []
    else:
        # print('Do not searching sub file folders ...... ')
        if textinfo:
            Text.configure(state='normal')
            Text.insert('end', '-' * 110 + '\n')
            Text.insert('end',_('* Do not searching sub file folders ...... \n'), "tag_purple")
            Text.configure(state='disabled')
        pathlist = []
        filenamelist = os.listdir(filepath)
        for i in range(len(filenamelist)):
            absfilepath = filepath + '/' + filenamelist[i]
            pathlist.append(absfilepath)

    # print('  The number of file paths is {}'.format(len(pathlist)))
    if textinfo:
        Text.configure(state='normal')
        Text.insert('end',_('The number of file paths is {}\n').format(len(pathlist)))
        Text.configure(state='disabled')

    for k in range(len(pathlist)):
        Text.configure(state='normal')
        # a=input('Continue ?')
        check1 = False    # the flag denote whether the file end with extension we input
        for indexitem in indexset:
            if pathlist[k].endswith(indexitem):
                check1 = True
        # print(pathlist[k])
        # print('Was it the file we want ?', "\033[1;34m {}  \033[0m".format(check1))
        if textinfo:
            Text.insert('end', pathlist[k] + '\n')
            Text.insert('end',_('Was it the file we want?').format(check1),"tag_B")

            if check1:
                Text.insert('end', " {} \n".format(_('Yes')), "tag_G")
            else:
                Text.insert('end', " {} \n".format(_('No')), "tag_Tomato")
        if check1:
            filepath = pathlist[k]
            # Call function to calculate the single file
            wordnumber, timecost, rate, success_flag = calculate_word(filepath, Text)
            if success_flag == 0:
                wordnumber = 0
                timecost = 1
                rate = 1
            wordnumber_sum.append(wordnumber)
            pathselect_sum.append(filepath)
            fileselect_sum.append(filenamelist[k])
            subtitlerate_sum.append(rate)
            timecostsum.append(timecost)
    # Here, the data haven't been sorted -------------------------------
    # print('-------------------------  take a list  -------------------------------')
    # print('The number of file selected is {}'.format(len(fileselect_sum)))
    Text.configure(state='disabled')
    # if textinfo:
    #     Text.insert('end', _('*  List ...... \n'),"tag_purple")
    #     Text.insert('end', _('The number of file selected is {}\n').format(len(fileselect_sum)))
    # for j in range(len(fileselect_sum)):
    #     # print('the filename is :          {}'.format(fileselect_sum[j]))
    #     # print('the sum of word number is :{}'.format(wordnumber_sum[j]))
    #     # print('the subtitle rate is :     {}'.format(subtitlerate_sum[j]))
    #     # print('the timecostsum is :     {}'.format(timecostsum[j]))
    #     if textinfo:
    #         Text.insert('end', _('-> the filename is :       {}\n').format(fileselect_sum[j]))
    #         Text.insert('end', _('the sum of word number is :{}\n').format(wordnumber_sum[j]))
    #         Text.insert('end', _('the subtitle rate is :     {}\n').format(subtitlerate_sum[j]))

    print('-------------------------- get the new name and new path ----------------------')
    if textinfo:
        Text.configure(state='normal')
        Text.insert('end',_('*  Get the new name and new path ......\n'),"tag_purple")
        Text.configure(state='disabled')
    oldNamelist, newNamelist, newNameRanksum, rateRankref = get_name(subtitlerate_sum, pathselect_sum, fileselect_sum)
    # Have data ranked
    oldnameRanksum, rateRanksum, timecostRanksum, wordnumberRanksum = rank_data(rateRankref, fileselect_sum, subtitlerate_sum,
                                                                               wordnumber_sum, timecostsum)
    # print(oldnameRanksum, rateRanksum, timecostRanksum,wordnumberRanksum)
    print('--------------------------- Write the txt file -------------------------------------')
    if textinfo:
        Text.configure(state='normal')
        Text.insert('end', _('*  Write the txt file  ......\n'), "tag_purple")
        Text.configure(state='disabled')
    write_txt(txtpath,savetxtflag,subtitlerate_sum,rateRankref,fileselect_sum)
    print('---------------------------- Rename or recover --------------------------------------')
    if textinfo:
        Text.configure(state='normal')
        Text.insert('end', _('*  Rename or recover ......\n'), "tag_purple")
        Text.configure(state='disabled')
    # for i in range(len(oldNamelist)):
    #     print(oldNamelist[i])
    #     print(newNamelist[i])
    rename_fun(oldNamelist, newNamelist, renameflag, Text)
    end = time.time()
    runtime = end - start
    print('>>>>>  The total running time is {:.4f} s'.format(runtime))
    if textinfo:
        Text.configure(state='normal')
        Text.insert('end',_('>>>>>  The total running time is {:.3f} s\n').format(runtime),"tag_purple")
        Text.insert('end', '-' * 110 + '\n')
        Text.configure(state='disabled')
    return fileselect_sum, wordnumber_sum, subtitlerate_sum, runtime, oldNamelist, newNamelist, \
        newNameRanksum, oldnameRanksum, rateRanksum, timecostRanksum, wordnumberRanksum
