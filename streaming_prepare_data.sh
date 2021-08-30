#!/bin/bash 
# bin/workloads/streaming/wordcount/prepare/genSeedDataset.sh &
bin/workloads/streaming/identity/prepare/genSeedDataset.sh &
bin/workloads/streaming/repartition/prepare/genSeedDataset.sh &
bin/workloads/streaming/fixwindow/prepare/genSeedDataset.sh



