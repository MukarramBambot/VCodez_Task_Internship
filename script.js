document.getElementById('suggestBtn').addEventListener('click', function() {
  const time = document.getElementById('timeSelect').value;
  const message = document.getElementById('mealMessage');

  if (time === 'morning') {
    message.textContent = "Breakfast: Try pancakes!";
  } else if (time === 'afternoon') {
    message.textContent = "Lunch: Enjoy a fresh salad!";
  } else if (time === 'evening') {
    message.textContent = "Dinner: Pasta is a great choice!";
  } else {
    message.textContent = "Snack time!";
  }
});


src="script.js"