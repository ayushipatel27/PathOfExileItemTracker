// Author: Tarra Kuhn

// Refreshes the data on the page.
function refresh(){
  $.get('/marketItems', $('#chooser').serialize()).then(response => {
    // The header looks dumb on its own, let's hide it if there's no rows.
    if (response.market.length == 0){
      $('#market-header').hide();
    }
    else{
      $('#market-header').show();

    }
    // Get rid of the old data
    $('.loaded').remove();
    for (row of response.market) {
      // Add the new rows to the table
      addRow(row);
    }
  });
}

// Adds a row to the market table
function addRow(row){
  $('#market-header').after(
    $('<tr>').append(`
      <!--<td class="first-td">${row.selling}</td>-->
      <td class="first-td"><img src="${row.image}"></td>
      <td>${row.val1}</td>
      <td>for</td>
      <td>${row.val2}</td>
      <td><img src="${row.buying}"></td>
      <td>${row.name}</td>
      <td>${row.league}</td>
      <td>${row.quantity}</td>
      <!--<td>${row.date}</td>-->
    `).addClass('loaded')
  )
}
// Wait for the document to load
$(document).ready(() => {
   // Refresh the page first thing
  refresh();
    // And when they click the search button, refresh again
  $('#search-btn').click(() => {
    refresh();
  })
})

// Update every 10 seconds
setInterval(() => {
  refresh();
}, 10000);



