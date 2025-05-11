file = open('youtube.txt', 'w')

try:
    file.write('Hare krishna')
finally:
    file.close()
    
with open('youtube.txt', 'w') as file:
    file.write('Hare Ram')