#!/bin/bash
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 默认的flink配置下，执行hibench的streaming程序
    pro=`/home/lemaker/open-source/kafka_2.12-2.8.0/bin/kafka-topics.sh --zookeeper localhost:2181 --list|awk '{print $1}'`
    j=0
    str=$1
    declare -a topic
    for i in $pro
    do
       if [[ $i =~ $str ]]
       then
           topic[$j]=$i
           let j=j+1
       fi
    done
    #### 输出数组的最后一个值，也就是最新的topic
   # echo ${topic[@]: -2}
    echo ${topic[-1]}

