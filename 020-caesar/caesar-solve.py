data = open("encrypted.txt").read();

for i in range(26):
    result = "";
    for char in data:
        result += chr(ord("a") + (ord(char) + i) % 26);
    print result;
