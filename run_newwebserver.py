import subprocess
import sys
import boto3

loop = 1

while loop == 1:
    # Menu to run
    print("Welcome to the run new web server program")
    print("Please select an option from the following:")
    print("")
    print("1) Create an EC2 instance")
    print("2) List instances")
    print("3) Terminate an instance")
    print("4) Check web server")
    print("5) Create an S3 bucket")
    print("6) List buckets")
    print("7) Copy image to bucket")
    print("8) Delete bucket contents")
    print("9) Delete a bucket")
    print("0) Exit!")

    choice = input("Choose your option:")
    choice = int(choice)

    if choice == 1:

    elif choice == 0:
        #Exit
        loop = 0
    else:
        print("ERROR!!! Please enter a valid option!")