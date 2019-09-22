

from app import app


if __name__ == '__main__':
    print("App server running at localhost:3000")
    app.run(debug=True, host='0.0.0.0', port='3000')