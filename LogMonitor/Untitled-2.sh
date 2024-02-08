#!/bin/bash

#declaring variables
TARGET="$1"                                               	 #The valid target file
DIR="export_forensics_results"							  	 # Main Directory to store the results
TARGET_SUBDIR="dir_${TARGET}"							   	 # Subdirectory to store results	
FILE_TRID="${DIR}/${TARGET_SUBDIR}/trid_${TARGET}"			 # File to store TRID results

# Create the main directory, if needed
if  [ -d "${DIR}" ]
then 
		echo -e "[+] Main directory already exists, skipping...\n"
else
		echo -e "[+] Creating main directory (/${DIR})\n"
		mkdir ${DIR}
fi

# create the subdirectory, if needed

if [ -d "${DIR}/${TARGET_SUBDIR}" ]
then
		echo -e "[+] Subdirectory already exists, skipping...\n"