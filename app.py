from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Dummy change to trigger CI

# In-memory database
items = []

def count_words(text: str) -> int:
    """Returns the number of words in the input text."""
    if not text or not isinstance(text, str):
        return 0
    return len(text.split())

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
