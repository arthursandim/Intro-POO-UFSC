casos = int(input())

while (casos<1 or casos>1000):
    casos = int(input())

for j in range(1,casos + 1):
    led = 0
    entrada = input()
    while(int(entrada) < 1 or int(entrada) > 10**100):
        entrada = input()
    for i in range(0,len(entrada)):
        if entrada[i] == '1':
            led = led + 2
        if entrada[i] == '2':
            led = led + 5
        if entrada[i] == '3':
            led = led + 5
        if entrada[i] == '4':
            led = led + 4
        if entrada[i] == '5':
            led = led + 5
        if entrada[i] == '6':
            led = led + 6
        if entrada[i] == '7':
            led = led + 3
        if entrada[i] == '8':
            led = led + 7
        if entrada[i] == '9':
            led = led + 6
        if entrada[i] == '0':
            led = led + 6
    print('{} leds'.format(led))