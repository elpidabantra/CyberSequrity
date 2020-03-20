import random
import multiprocessing
from multiprocessing import Pool
import sys
import statistics
import time
import os

# assume that all the messages come in the same year

def read_file(input_f):
	list_lines = []
	file = open(input_f, "r") 
	for line in file: 
		l = line.split(">")
		priority_value = l[0][1:]
		timestamp = l[1][0:15]
		MSG = l[1][17:]
		hostname = MSG.split(" ")[0]
		list_lines.append([priority_value,timestamp,hostname,len(MSG)])
	return list_lines


def create_stats(list_lines):
	
	total = 0	  
	MSG_l = []	 
	dic_h = {}   
	dic_len = {}
	d_t = []
	Mmm_d = {}
	dic_time = {} 
	dic_time_t = {}

	# dictionary of months
	Mmm_d["Jan"] = 1
	Mmm_d["Feb"] = 2
	Mmm_d["Mar"] = 3
	Mmm_d["Apr"] = 4
	Mmm_d["May"] = 5
	Mmm_d["Jun"] = 6
	Mmm_d["Jul"] = 7
	Mmm_d["Aug"] = 8
	Mmm_d["Sep"] = 9
	Mmm_d["Oct"] = 10
	Mmm_d["Nov"] = 11
	Mmm_d["Dec"] = 12
	

	for lis in list_lines:
		month = Mmm_d[str(lis[1].split(" ")[0])]
		day = lis[1].split(" ")[1][0:0]
		lll = lis[1].split(" ")
		if lll[1] == "":
			day = lis[1].split(" ")[2][0:1]
			time = lis[1].split(" ")[3]
		else:
			day = lis[1].split(" ")[1][0:2]
			time = lis[1].split(" ")[2]
		time = time.split(":")
		MSG_l.append(lis[3])
		dic_time_t[int(str(int(month))+str(int(day))+str(int(time[0]))+str(int(time[1]))+str(int(time[2])))] = lis[1]
		d_t.append(int(str(int(month))+str(int(day))+str(int(time[0]))+str(int(time[1]))+str(int(time[2]))))

		if lis[2] in dic_len:
			dic_len[lis[2]].append(lis[3])
			dic_time[lis[2]].append(int(str(int(month))+str(int(day))+str(int(time[0]))+str(int(time[1]))+str(int(time[2]))))
		else:
			dic_len[lis[2]] = [lis[3]]
			dic_time[lis[2]] = [int(str(int(month))+str(int(day))+str(int(time[0]))+str(int(time[1]))+str(int(time[2])))]

		if int(lis[0]) in [0,1,8,9,16,17,24,25,32,33,40,41,48,49,56,57,64,65,72,73,80,81,88,89,96,97,104,105,112,113,120,121,128,129,136,137,144,145,152,153,160,161,168,169,176,177,184,185]:
			total = total + 1
			if lis[2] in dic_h:
				dic_h[lis[2]] = dic_h[lis[2]] + 1
			else:
				dic_h[lis[2]] = 1


	########### print stats ##################	
	print("The total average MSG length is " + str(statistics.mean(MSG_l))+".")
	print("The total number of Emergency and Alert severity level messages is " + str(total)+"." )
	print("The oldest message came on " + str(dic_time_t[min(d_t)])+ " and the newest message came on " + str(dic_time_t[max(d_t)]) + " of the same year.")
	print(["HOSTNAME", "AVG_MSG_LENGTH", "number_of_Emergency_and_Alert_severity", "oldest message", "newest message"])
	for i in  dic_len:
		if i in dic_h:
			gg =  dic_h[i]
		else:
			gg =  0
		print([i, statistics.mean(dic_len[i]), gg, dic_time_t[min(dic_time[i])], dic_time_t[max(dic_time[i])] ])


if __name__ == "__main__":
	pathToFile = "/Users/elpidabantra/Desktop/Programming Task/solution"
	p = multiprocessing.Pool() # perform the same process on multiple files simultaneously
	t = []
	results = []
	for name in os.listdir(pathToFile):
		if name.endswith(".txt"):
			t.append(name)
	pool = Pool()
	results = pool.map(read_file, t)

	f = []
	for i in range(len(results)):
		f = f + results[i]

	create_stats(f)





