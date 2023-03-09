import speedtest
import pyfiglet
import csv
import datetime
import os
import sys

script_version = '0.2.0'


def performTests(iterations: int = 3) -> dict:
    print("Finding best server...")
    st = speedtest.Speedtest()
    st.get_best_server()
    print('Connected!')
    downloads: list[float] = []
    uploads: list[float] = []
    print('Performing {0} tests.'.format(iterations))
    for i in range(iterations):
        res_dict = {}
        print("Performing test", '{0}...'.format(str(i+1)))
        print("Download...")
        st.download()
        print("Upload...")
        st.upload()
        downloads.append(round(st.results.download / 1000000, 2))
        uploads.append(round(st.results.upload / 1000000, 2))

    averages = {
        'Time Taken': datetime.datetime.now(),
        'Download': sum(downloads) / len(downloads),
        'Upload': sum(uploads) / len(uploads)
    }
    return averages


def writeResultsToFile(results: dict):
    print('Writing to file...')
    with open('results.csv', 'w+') as csvFile:
        fieldnames = results.keys()
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

        writer.writeheader()
        # writer.writerows(results)
        writer.writerow(results)


def enterNumber() -> int:
    while True:
        testIterations = input('How many test iterations? (3): ')
        if testIterations.isnumeric():
            return int(testIterations)
        elif testIterations == '':
            testIterations = 3
            return testIterations
        elif testIterations == 'exit':
            print('Goodbye.')
            exit()
        else:
            print('Invalid number. Try again.')


print('\n')
pyfiglet.print_figlet("speed.py", 'banner3-d')
print(script_version, 'By Darren Meiring\n\n')

number_of_tests = enterNumber()

results = performTests(number_of_tests)

writeResultsToFile(results)

if sys.platform == "win32":
    os.startfile('results.csv')
elif sys.platform == "darwin":
    os.system('open results.csv')
else:
    print("Unknown OS")
