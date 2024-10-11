class TemperatureConverter:

    count = 0

    def fahrenheit(celsius):
        TemperatureConverter.count += 1
        return (celsius * 9/5) + 32

    def celsius(fahrenheit):
        TemperatureConverter.count += 1
        return (fahrenheit - 32) * 5/9

    def get_count():
        return TemperatureConverter.count


print(TemperatureConverter.fahrenheit(25))
print(TemperatureConverter.celsius(77)) 
print(TemperatureConverter.get_count())