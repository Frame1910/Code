import speedtest
import pyfiglet

st = speedtest.Speedtest()
st.get_best_server()


def performTests(iterations=3):
    results = []
    for i in range(iterations):
        res_dict = {}
        print('Performing {0} tests.'.format(iterations))
        print("Performing test", '{0}...'.format(str(i+1)))
        print("Download...")
        st.download()
        print("Upload...")
        st.upload()
        res_dict["download"] = round(st.results.download / 1000000, 2)
        res_dict["upload"] = round(st.results.upload / 1000000, 2)
        results.append(res_dict)
    return results


def writeResultsToFile(results):
    print('Writing to file...')
    with open('results.txt', 'w+') as f:
        for i, res in enumerate(results):
            test_number_text = 'Test {0}: \n'.format(i+1)
            download_text = 'Download: {0} mbps\n'.format(res['download'])
            upload_text = 'Upload: {0} mbps\n\n'.format(res['upload'])

            print(test_number_text)
            print(download_text)
            print(upload_text)
            f.write(test_number_text)
            f.write(download_text)
            f.write(upload_text)
        f.close()
    print('Done.')


def enterNumber():
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
print('v0.1.2', 'By Darren Meiring\n\n')

number_of_tests = enterNumber()

results = performTests(number_of_tests)

writeResultsToFile(results)
