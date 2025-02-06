from flask import Flask, request

app = Flask(__name__)

# query для функции query-example
# http://127.0.0.1:5000/query-example?language=Python&framework=Flask&website=localhost
@app.route("/query-example")
def query_example():
    # Если ключ отсутствует, то вернется None
    language = request.args.get('language')

    # Если ключ отсутствует, то вернется ошибка 404 Bad request
    framework = request.args["framework"]

    # Если ключ отсутствует, то вернется None
    website = request.args.get('website')

    return (''' 
                <h1>The language value is {}</h1>
                <h1>The framework value is {}</h1>
                <h1>The website value is {}</h1>'''.format(language, framework, website))


@app.route("/form-example", methods=["GET", "POST"])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                <h1>The language value is: {}</h1> 
                <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''
        <form method="POST">
            <div><label>Language: <input type="text" name="language"</label></div>
            <div><label>Framework: <input type="text" name="framework"</label></div>
            <input type="submit" value="Отправить">
        </form>
        '''


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']
        if 'framework' in request_data:
            framework = request_data['framework']
        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']
        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]
        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']
    return '''  
                The language value is: {}   
                The framework value is: {}   
                The Python version is: {}  
                The item at index 0 in the example list is: {}  
                The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
