from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    algorithm = request.form.get('algorithm')
    if algorithm == 'heap':
        import heart_heap
        heart_heap.main()  # Generate and save the graph
    elif algorithm == 'quick':
        import heart_quick
        heart_quick.main()  # Generate and save the quicksort graph
    elif algorithm == 'merge':
        import heart_merge
        heart_merge.main()
    elif algorithm == 'bubble':
        import heart_bubble
        heart_bubble.main()
    else:
        return "Invalid algorithm selected.", 400
    return "Graph generated successfully!", 200


if __name__ == "__main__":
    app.run(debug=True)
