from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	return render_template('index.html', count=visitors_count)

@app.route('/', methods=['post'])
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	data = request.form['text']
	stats = 'https://covid-api-262.herokuapp.com/?country='+data

	return render_template('index.html', image=stats, count=visitors_count)

if  __name__ == '__main__':
	app.run()