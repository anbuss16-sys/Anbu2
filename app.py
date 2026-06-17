from flask import Flask, request
from prime import primes_upto

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <h2>Prime Number Finder</h2>

    <form action="/primes" method="get">
        <input type="number" name="limit" placeholder="Enter limit" required>
        <button type="submit">Find Primes</button>
    </form>
    """


@app.route("/primes")
def find_primes():

    try:
        limit = int(request.args.get("limit"))

        result = primes_upto(limit)

        return f"""
        <h2>Prime Numbers</h2>

        <p>Prime numbers up to {limit}:</p>

        <p>{result}</p>

        <a href="/">Try Another</a>
        """

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
