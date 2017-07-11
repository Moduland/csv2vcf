# -*- coding: utf-8 -*-
import os
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

def zero_insert(input_string):
    '''
    This function get a string as input if input is one digit add a zero
    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    '''
    if len(input_string)==1:
        return "0"+input_string
    return input_string

def time_convert(input_data):
    '''
    This function convert input_sec  from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=input_data
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds"

def VCF_init(file):
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")

def VCF_name(file,first_name,last_name):
    file.write("N:"+last_name+";"+first_name+";;;"+"\n")
    file.write("FN:" + first_name+" "+last_name + "\n")

def VCF_phone(file,tel_mobile,tel_home,tel_work):
    file.write("TEL;type=CELL:" + tel_mobile + "\n")
    file.write("TEL;type=HOME:" + tel_home + "\n")
    file.write("TEL;type=WORK:" + tel_work + "\n")

def VCF_email(file,email_home,email_mobile,email_work):
    file.write("EMAIL;type=INTERNET;type=WORK;type=pref:" + email_work + "\n")
    file.write("EMAIL;type=INTERNET;type=HOME;type=pref:" + email_home + "\n")
    file.write("EMAIL;type=INTERNET;type=CELL;type=pref:" + email_mobile + "\n")


def VCF_adr(file,adr_work,adr_home):
    file.write('item1.ADR;type=WORK:;; ' + adr_work + "\n")
    file.write('item2.ADR;type=HOME;type=pref:;; ' + adr_home + "\n")

def VCF_website(file,website_url):
    file.write('item3.URL;type=pref:' + website_url + "\n")
    file.write("END:VCARD")
    file.close()

def VCF_Folder(filename):
    folder_adr=os.path.dirname(filename)
    filename_split=filename.split("/")[-1].split(".")[0]
    VCF_folder_adr = os.path.join(folder_adr, "VCF_CONVERT_" + filename_split)
    if "VCF_CONVERT_"+filename_split not in os.listdir(folder_adr):
        os.mkdir(VCF_folder_adr)
    return VCF_folder_adr

def VCF_creator(folder_name,first_name,last_name,tel_mobile,tel_home,tel_work,email_home,email_work,email_mobile,adr_work,adr_home,website_url):
    file=open(os.path.join(folder_name,last_name+"_"+first_name+".vcf"),"w")
    VCF_init(file)
    VCF_name(file,first_name,last_name)
    VCF_phone(file,tel_mobile,tel_home,tel_work)
    VCF_email(file,email_home,email_mobile,email_work)
    VCF_adr(file,adr_work,adr_home)
    VCF_website(file,website_url)

def csv_reader(file_name):
    try:
        file=open(file_name,"r")
        unknown_index=0
        vcf_counter=0
        name_dict={}
        foldername=VCF_Folder(file_name)
        for index,line in enumerate(file):
            if index>0:
                stripped_line=line.strip()
                temp=stripped_line.split(",")
                if len(temp)>11:
                    print("[Warning] CSV File Line "+str(index)+" Bad Format")
                    continue
                else:
                    name=temp[0]+","+temp[1]
                    if name not in name_dict.keys():
                        name_dict[name]=0
                    else:
                        name_dict[name]=name_dict[name]+1
                    if len(temp[0])==0 and len(temp[1])==0:
                        unknown_index+=1
                        VCF_creator(foldername,"Unknown ",str(unknown_index),temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10])
                    else:
                        if name_dict[name]!=0:
                            VCF_creator(foldername,temp[0]+"_"+str(name_dict[name]),temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10])
                        else:
                            VCF_creator(foldername, temp[0], temp[1], temp[2], temp[3],temp[4], temp[5], temp[6], temp[7], temp[8], temp[9], temp[10])
                    vcf_counter+=1
        return vcf_counter

    except FileNotFoundError:
        print("[Warning] Please Open CSV File")
    except Exception as e:
        messagebox.showinfo("CSV2VCF", "Error In Reading Input File")
        print("[Error] In Reading Input File")

