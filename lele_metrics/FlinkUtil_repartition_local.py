
import os
import math
import time


#transform str to int/float
#to generate proper bound for local search
#input:30 conf(list)
#output:30 conf(list)
def inversion(conf):
    result=[]
    for i in range(0,14):
        result.append(int(conf[i]))
    temp=int(math.log(int(conf[14]),2))
    result.append(temp)
    result.append(1)
    result.append(1)
    for i in range(17,21):
        result.append(int(conf[i]))
    result.append(1)
    for i in range(22,27):
        result.append(int(conf[i]))
    result.append(1)
    result.append(1)
    return result


def getConfigure(path, string, raw):
    with open(path, 'r') as file_to_read:
        lines = file_to_read.readlines()
        file_to_read.seek(0)
        value = lines[raw - 1].split()[-1]
        file_to_read.close()
    return value

def getKafkatopic(pro):
    # HIBENCH_HOME = os.getenv('HIBENCH_HOME')
    HIBENCH_HOME="/home/lemaker/open-source/HiBench-7.0"

    produceNum = getConfigure(HIBENCH_HOME+'/conf/hibench.conf', 'hibench.streambench.datagen.producerNumber', 114)
    recordPerInterval = getConfigure(HIBENCH_HOME+'/conf/hibench.conf', 'hibench.streambench.datagen.recordsPerInterval', 110)
    print("produceNum:"+produceNum)
    print("recordPerInterval"+recordPerInterval)
    intervalSpan = getConfigure(HIBENCH_HOME+'/conf/hibench.conf', 'hibench.streambench.datagen.intervalSpan', 108)
    print("intervalSpan:"+intervalSpan)
    recordsPreSecond = int(recordPerInterval) * 1000 * int(produceNum) / int(intervalSpan)
    string = 'FLINK_' + pro + '_' + produceNum + '_' + recordPerInterval + '_' + intervalSpan
    topic = os.popen("bash "+HIBENCH_HOME+"/lele_metrics/getWholeKafkaTopic_local.sh "+string)
    reportTopic = topic.read().split('\n')[0]
    topic.close()
    return reportTopic

def runProgram(pro,duration):
    # HIBENCH_HOME= os.getenv('HIBENCH_HOME')
    # HIBENCH_HOME="/home/lemaker/open-source/HiBench-7.0-three"
    HIBENCH_HOME = "/home/lemaker/open-source/HiBench-7.0"

    print("==== fetching metrics ======")
    topic = getKafkatopic(pro)
    print("====== topic is " + topic + "======")
    cnt=0
    while cnt<=20:
        cnt=cnt+1
        print("iteration {}".format(cnt))
        os.system("bash "+HIBENCH_HOME+"/bin/workloads/streaming/" + pro + "/common/metrics_reader.sh "+topic)
        time.sleep(duration) # 休眠duration秒
  
    #os.system("bash "+FLINKTUNER_HOME+"/Code/util/deleteKafkaTopic.sh "+pro)

def configure(path, string, raw, value):
    with open(path, 'r+') as file_to_read:
        lines = file_to_read.readlines()
        file_to_read.seek(0)
        file_to_read.truncate()
        lines[raw - 1] = string + '          ' + str(value) + '\n'
        file_to_read.writelines(lines)
        file_to_read.close()


if __name__ == '__main__':
    runProgram("repartition",10)