
import stripe
stripe.api_key = "sk_test_mNE4jbeT6xdwRv7YWmOXe8oa"

stripe.Charge.create(
  amount=2000,
  currency="usd",
  source="tok_visa", # obtained with Stripe.js
  description="Charge for Khushal"
)

print("Hello, World!")