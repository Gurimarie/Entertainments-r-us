/* 
From Boutique Ado Code Institute-project.
Stripe payments, core logic: 
https://stripe.com/docs/payments/accept-a-payment

CSS:
https://stripe.com/docs/payments/elements
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1. -1);  // slice to remove quotationmarks
var client_secret = $('#id_client_secret').text().slice(1. -1);  // slice to remove quotationmarks
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');
