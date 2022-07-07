

/* 
From Boutique Ado Code Institute-project.
Stripe payments, core logic: 
https://stripe.com/docs/payments/accept-a-payment

CSS:
https://stripe.com/docs/payments/elements
*/


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);  // slice to remove quotationmarks
var clientSecret = $('#id_client_secret').text().slice(1, -1);  // slice to remove quotationmarks

var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');

// handle realtime-validation-errors on the card-element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error_message}</span>
            `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form-submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            // show error to your customer
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error_message}</span>
            `;
            $(errorDiv).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                // the payment has been processed
                form.submit();
            }
        }
    });
});
