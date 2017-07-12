# -*- coding: utf-8 -*-
import os
from tkinter import messagebox

name_dict={}
unknown_index=0
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
    '''
    This function add static part of VCF
    :param file: file object
    :return: None
    '''
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")

def VCF_name(file,first_name,last_name):
    '''
    This function add names to VCF file
    :param file: file object
    :param first_name: Name
    :type first_name:str
    :param last_name: Name
    :type last_name:str
    :return: None
    '''
    file.write("N:"+last_name+";"+first_name+";;;"+"\n")
    file.write("FN:" + first_name+" "+last_name + "\n")

def VCF_phone(file,tel_mobile,tel_home,tel_work):
    '''
    This function add numbers
    :param file: file object
    :param tel_mobile: mobile number
    :type tel_mobile:str
    :param tel_home: home number
    :type tel_home:str
    :param tel_work: work number
    :type tel_work:str
    :return: None
    '''
    file.write("TEL;type=CELL:" + tel_mobile + "\n")
    file.write("TEL;type=HOME:" + tel_home + "\n")
    file.write("TEL;type=WORK:" + tel_work + "\n")

def VCF_email(file,email_home,email_mobile,email_work):
    '''
    This function add emails
    :param file: file object
    :param email_home: Email
    :type email_home:str
    :param email_mobile: Email
    :type email_mobile:str
    :param email_work: Email
     :type email_work:str
    :return: None
    '''
    file.write("EMAIL;type=INTERNET;type=WORK;type=pref:" + email_work + "\n")
    file.write("EMAIL;type=INTERNET;type=HOME;type=pref:" + email_home + "\n")
    file.write("EMAIL;type=INTERNET;type=CELL;type=pref:" + email_mobile + "\n")


def VCF_adr(file,adr_work,adr_home):
    '''
    This function add Address
    :param file: file object
    :param adr_work: Address
    :type adr_work:str
    :param adr_home: Address
    :type adr_home;str
    :return: None
    '''
    file.write('item1.ADR;type=WORK:;; ' + adr_work + "\n")
    file.write('item2.ADR;type=HOME;type=pref:;; ' + adr_home + "\n")

def VCF_website(file,website_url):
    '''
    This function add website url
    :param file: file object
    :param website_url: URL
    :type website_url:str
    :return: None
    '''
    file.write('item3.URL;type=pref:' + website_url + "\n")
    file.write("END:VCARD")
    file.close()

def VCF_Folder(filename):
    '''
    This function create VCF folder from file name
    :param filename: input file name
    :type filename:str
    :return: VCF_folder_adr as str
    '''
    folder_adr=os.path.dirname(filename)
    filename_split=filename.split("/")[-1].split(".")[0]
    VCF_folder_adr = os.path.join(folder_adr, "VCF_CONVERT_" + filename_split)
    if "VCF_CONVERT_"+filename_split not in os.listdir(folder_adr):
        os.mkdir(VCF_folder_adr)
    return VCF_folder_adr

def VCF_creator(folder_name,first_name,last_name,tel_mobile,tel_home,tel_work,email_home,email_work,email_mobile,adr_work,adr_home,website_url):
    '''
    This function create VCF files
    :param folder_name: Folder name
    :param first_name: Name
    :param last_name:  Name
    :param tel_mobile: tel
    :param tel_home: Tel
    :param tel_work: Tel
    :param email_home: Email
    :param email_work:Email
    :param email_mobile: Email
    :param adr_work: Address
    :param adr_home: Address
    :param website_url: URL
    :return: None
    '''
    file=open(os.path.join(folder_name,last_name+"_"+first_name+".vcf"),"w")
    VCF_init(file)
    VCF_name(file,first_name,last_name)
    VCF_phone(file,tel_mobile,tel_home,tel_work)
    VCF_email(file,email_home,email_mobile,email_work)
    VCF_adr(file,adr_work,adr_home)
    VCF_website(file,website_url)

def name_dict_update(name):
    '''
    This function save number of each name
    :param name: input name
    :type name:str
    :return:None
    '''
    global name_dict
    if name not in name_dict.keys():
        name_dict[name] = 0
    else:
        name_dict[name] = name_dict[name] + 1

def VCF_write(temp,name_dict,foldername):
    '''
    This function write VCF files in loop (call VCF_creator)
    :param temp: list of each row information
    :type temp:list
    :param name_dict: dictionary of each name number
    :type name_dict:dict
    :param foldername: folder name
    :type foldername:str
    :return: None
    '''
    name = temp[0] + "," + temp[1]
    name_dict_update(name)
    global unknown_index
    if len(temp[0]) == 0 and len(temp[1]) == 0:
        unknown_index += 1
        VCF_creator(foldername, str(unknown_index),"Unknown ", temp[2], temp[3], temp[4], temp[5], temp[6], temp[7],
                    temp[8], temp[9], temp[10])
    else:
        if name_dict[name] != 0:
            VCF_creator(foldername, temp[0] + "_" + str(name_dict[name]), temp[1], temp[2], temp[3], temp[4], temp[5],
                        temp[6], temp[7], temp[8], temp[9], temp[10])
        else:
            VCF_creator(foldername, temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8],
                        temp[9], temp[10])
def csv_reader(file_name):
    '''
    This function read input csv file and parse it
    :param file_name: file name or address of file
    :type file_name:tr
    :return: vcf_counter as integer
    '''
    try:
        file=open(file_name,"r")

        vcf_counter=0

        foldername=VCF_Folder(file_name)
        for index,line in enumerate(file):
            if index>0:
                stripped_line=line.strip()
                temp=stripped_line.split(",")
                if len(temp)>11:
                    print("[Warning] CSV File Line "+str(index)+" Bad Format")
                    continue
                else:
                    VCF_write(temp,name_dict,foldername)
                    vcf_counter+=1
        return vcf_counter

    except FileNotFoundError:
        print("[Warning] Please Open CSV File")
    except Exception:
        messagebox.showinfo("CSV2VCF", "Error In Reading Input File")
        print("[Error] In Reading Input File")

