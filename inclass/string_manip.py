config = 'SET portal "US"\nSET textLocal "enUS"\nSET audioLocal "enUS"'
commands = []

l_index = 0
r_index = config.find('\n')

while r_index != -1:
    commands.append(config[l_index:r_index])
    l_index = r_index + 1
    r_index = config.find('\n', l_index)
commands.append(config[l_index])

print(commands)

result = []
for cmd in commands:
    data-[]
    l_index = 0

    while ' ' in cmd[l_index:] == True:
        r_index = cmd.index(' ', l_index)
        data.append(cmd[l_index:r_index])
        l_index = r_index + 1

    data.append(cmd[l_index:])
    result.append(data)
