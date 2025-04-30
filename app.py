from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def convert_number(number, from_base, to_base):
    """
    Convert a number from one base to another.
    """
    # First convert to decimal (base 10)
    try:
        if from_base == 'Binary':
            decimal = int(number, 2)
        elif from_base == 'Octal':
            decimal = int(number, 8)
        elif from_base == 'Hexadecimal':
            decimal = int(number, 16)
        else:  # Decimal
            decimal = int(number)

        # Then convert decimal to target base
        if to_base == 'Binary':
            return bin(decimal)[2:]  # Remove '0b' prefix
        elif to_base == 'Octal':
            return oct(decimal)[2:]  # Remove '0o' prefix
        elif to_base == 'Hexadecimal':
            return hex(decimal)[2:].upper()  # Remove '0x' prefix and convert to uppercase
        else:  # Decimal
            return str(decimal)
    except ValueError:
        return None

@app.route('/')
def index():
    number_systems = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']
    return render_template('index.html', number_systems=number_systems)

@app.route('/convert', methods=['POST'])
def convert():
    number_systems = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']
    
    number = request.form.get('number', '').strip()
    from_system = request.form.get('from_system')
    to_system = request.form.get('to_system')
    
    result = convert_number(number, from_system, to_system)
    
    if result is not None:
        message = f"{number} ({from_system}) = {result} ({to_system})"
        error = None
    else:
        message = None
        error = f"Invalid {from_system} number entered. Please try again."
    
    return render_template('result.html', 
                          number_systems=number_systems,
                          number=number, 
                          from_system=from_system, 
                          to_system=to_system,
                          result=result,
                          message=message,
                          error=error)

if __name__ == '__main__':
    app.run(debug=True)
