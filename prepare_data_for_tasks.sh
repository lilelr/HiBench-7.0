#!/bin/bash 
bin/workloads/micro/wordcount/prepare/prepare.sh &
bin/workloads/micro/sort/prepare/prepare.sh &
bin/workloads/micro/terasort/prepare/prepare.sh
bin/workloads/websearch/pagerank/prepare/prepare.sh 
bin/workloads/graph/nweight/prepare/prepare.sh 



