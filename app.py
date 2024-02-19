import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

count_file = "counter.txt"
if 'COUNTER_FILE' in os.environ.keys():
    count_file = os.environ["COUNTER_FILE"]


def read_counter():
    if os.path.isfile(count_file):
        fp = open(count_file)
        b = fp.read()
        fp.close()
        return int(b)
    else:
        return 0


total_visitors = read_counter()


def write_counter():
    fp = open(count_file, "w")
    fp.write(str(total_visitors))
    fp.close()


@app.route('/')
def hello():
    global total_visitors
    total_visitors = total_visitors + 1
    return f'Hello, World! you are visitor number {total_visitors}'


@app.teardown_appcontext
def shutdown_session(exception=None):
    write_counter()


if __name__ == '__main__':
    app.run(debug=True)


# building docker image
# docker build -t myflaskapp .
#