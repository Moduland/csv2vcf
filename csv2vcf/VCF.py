# -*- coding: utf-8 -*-
import os

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



def VCF_creator(first_name,last_name,tel_mobile,tel_home,tel_work,email_home,email_work,email_mobile):
    if "VCF_CONVERT" not in os.listdir():
        os.mkdir("VCF_CONVERT")
    file=open(os.path.join("VCF_CONVERT",last_name+"_"+first_name+".vcf"),"w")
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")
    file.write("N:"+last_name+";"+first_name+";;;"+"\n")
    file.write("FN:" + first_name+" "+last_name + "\n")
    file.write("TEL;type=CELL:"+tel_mobile+"\n")
    file.write("TEL;type=HOME:" + tel_home + "\n")
    file.write("TEL;type=WORK:" + tel_work + "\n")
    file.write("EMAIL;type=INTERNET;type=WORK;type=pref:"+email_work+"\n")
    file.write("EMAIL;type=INTERNET;type=HOME;type=pref:" + email_home + "\n")
    file.write("EMAIL;type=INTERNET;type=CELL;type=pref:" + email_mobile + "\n")
    file.write("END:VCARD")
    file.close()
def csv_reader(file_name):
    try:
        file=open(file_name,"r")
        unknown_index=0
        vcf_counter=0
        for index,line in enumerate(file):
            if index>0:
                stripped_line=line.strip()
                temp=stripped_line.split(",")
                if len(temp)>8:
                    print("[Warning] CSV File Line "+str(index)+" Bad Format")
                    continue
                else:
                    if len(temp[0])==0 and len(temp[1])==0:
                        unknown_index+=1
                        VCF_creator("Unknown ",str(unknown_index),temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
                    else:
                        VCF_creator(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
                    vcf_counter+=1
        return vcf_counter

    except Exception as e:
        print("[Error] In Reading CSV File")

