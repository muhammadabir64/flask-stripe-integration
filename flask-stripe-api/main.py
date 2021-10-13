from flask import Flask, request, render_template, url_for
import stripe

app = Flask(__name__)

stripe_keys = {
  'secret_key': "",
  'publishable_key': ""
  }
stripe.api_key = stripe_keys['secret_key']


@app.route("/")
def home():
	return render_template("home.html", key=stripe_keys['publishable_key'])


@app.route("/purchase", methods=["POST"])
def purchase():
	customer = stripe.Customer.create(
	    source=request.form['stripeToken']
	)
	charge = stripe.Charge.create(
	    customer=customer.id,
	    amount=request.form['amount'],
	    currency='usd',
	)
	return "thank you for make your purchase"


if __name__ == "__main__":
	app.run(debug=True)