/*let tg = window.Telegram.WebApp;
tg.expand();
const user = tg.initDataUnsafe.user;

if (user) {
    const userData = {
        user_id: user.id.toString(),
        username: user.username || '',
        first_name: user.first_name || '',
        last_name: user.last_name || ''
    };

    fetch('http://127.0.0.1:8000/save_user/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
        .then(response => response.json())
        .then(data => console.log('User saved:', data))
        .catch(error => console.error('Error saving user', error));

}
*/
//document.getElementById('showProducts').addEventListener('click', function(){

fetch('http://127.0.0.1:8000/products/', {
    method: 'GET',
})
    .then(response => response.json())
    .then(data => {
        if (data.products) {
            let productHtml = '';
            data.products.forEach(product => {
                productHtml += '<div class="img-conteiner ratio4"><img class="preview-img-portrait" src="http://127.0.0.1:8000/static/slavichoney_app/images/' + product.image + '"> </div>';
                productHtml += '<p class="pL">' + product.product_name + '<br>';
                productHtml += product.price + ' ₽ <br>';
                productHtml += 'Категория: ' + product.category + '<br>';
                productHtml += product.description + '<br></p>';
            });
            document.getElementById('products').innerHTML = productHtml;
        }
        else {
            alert('В базе нет продуктов');
        }
    })
    .catch(error => {
        console.error('Error', error);
        alert('Ошибка при получении продуктов');
    });
//});
/*
<div class="img-conteiner ratio1">
          <a href="#"><img class="preview-img-portrait" src="images/previewIdentityCorporateStationeryOrange.jpg"
              alt="identityCorporateStationeryOrange"></a>
        </div>
        */