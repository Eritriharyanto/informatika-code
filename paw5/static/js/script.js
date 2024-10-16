document.getElementById('purchaseBtn').addEventListener('click', function() {
    let item = document.getElementById('itemSelect').value;
    let quantity = parseInt(document.getElementById('quantityInput').value);
    let resultDiv = document.getElementById('result');

    // clear previous result
    resultDiv.innerHTML = '';

    if (quantity > 0) {
        //ajax request to purchase item
        fetch('/purchase', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ item: item, quantity: quantity})    
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                resultDiv.innerHTML = data.message;
            } else if (data.error) {
                resultDiv.innerHTML = data.error;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = 'Error processing request.';
            console.error('Error', error);
        });
    } else {
        resultDiv.innerHTML = 'Please enter a valid quantity.';
    }
});