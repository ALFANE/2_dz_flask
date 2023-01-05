from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/<name>')
def Hello(name = 'Evhenii'):
    return render_template(
        'index.html',
        name_t=name
    )

@app.route('/encrypt')
def encrypt():
    result = "Encrypt result: "
    string_to_encrypt = request.args.get('string')
    string_to_encrypt = (f.encrypt(string_to_encrypt.encode())).decode()
    return render_template(
        'index.html',
        result_t=result,
        string_t = string_to_encrypt
    )

@app.route('/decrypt')
def decrypt():
    result = "Decrypt result: "
    string_to_decrypt = request.args.get('string')
    string_to_decrypt = (f.decrypt(string_to_decrypt.encode())).decode()
    return render_template(
        'index.html',
        result_t=result,
        string_t = string_to_decrypt
    )




if __name__ == '__main__':
    app.run(debug=True)