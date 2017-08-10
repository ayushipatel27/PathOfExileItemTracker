function refresh(){
  $.get('/marketItems', $('#chooser').serialize()).then(response => {
    if (response.market.length == 0){
      $('#market-header').hide();
    }
    else{
      $('market-header').show();
    }
    $('.loaded').remove();
    for (row of response.market) {
      addRow(row);
    }
  });
}

function addRow(row){
  $('#market-header').after(
    $('<tr>').append(`
      <td>${row.selling}</td>
      <td><img src="${row.image}"></td>
      <td>${row.val1}</td>
      <td>for</td>
      <td>${row.val2}</td>
      <td>${row.buying}</td>
      <td>${row.name}</td>
      <td>${row.league}</td>
      <td>${row.quantity}</td>
      <td>${row.date}</td>
    `).addClass('loaded')
  )
}
$(document).ready(() => {
  refresh();
  $('#search-btn').click(() => {
    refresh();
  })
})

setInterval(() => {
  refresh();
}, 10000);


console.log("Market.js loading")
