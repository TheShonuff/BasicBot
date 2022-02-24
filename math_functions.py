def rect_to_polar():
    a = input("Input resistor value: ")
    b = input("input capacitive reactance value: ")

    magnitude = math.sqrt((int(a)**2) + (int(b)**2))
    print(magnitude)

    phase_angle = math.degrees(math.atan(int(b)/int(a)) )
    print(phase_angle)

    print(f'Z = {magnitude} \u2221 {phase_angle}')


def convertPolar2(ctx):
        
        await ctx.send('Input resistor value: ')
        message_response = await bot.wait_for('message')
        a = (message_response.content)
        
        await ctx.send('Input capacitive reactance value: ')
        message_response = await bot.wait_for('message')
        b = (message_response.content)

        # a = input("Input resistor value: ")
        # b = input("input capacitive reactance value: ")

        magnitude = math.sqrt((int(a)**2) + (int(b)**2))
        print(magnitude)

        phase_angle = math.degrees(math.atan(int(b)/int(a)) )
        print(phase_angle)

        # result = print(f'Z = {magnitude} \u2221 {phase_angle}')
        
        await ctx.send(f'z = {magnitude} \u2221 {phase_angle}')