// Initialize total income and total expenses
let totalIncome = 0;
let totalExpenses = 0;

// Function to add income
function addIncome() {
    // Prompt user for income
    let amount = prompt('Enter Income:');
    totalIncome += +amount;

    // Display a message with the updated total income
    document.write('Total Income: ' + totalIncome + '<br><br>');
}

// Function to add expense
function addExpense() {
    // Prompt user for expense
    let amount = prompt('Enter Expense:');
    totalExpenses += +amount;

    // Display a message with the updated total expenses
    document.write('Total Expenses: ' + totalExpenses + '<br><br>');
}

// Function to display remaining budget
function displayRemainingBudget() {
    // Calculate remaining budget by subtracting expenses from income
    let remainingBudget = totalIncome - totalExpenses;

    // Display the remaining budget
    document.write('Remaining Budget: ' + remainingBudget + '<br><br>');
}


addIncome();
addExpense();
displayRemainingBudget();