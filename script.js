// Set the countdown time in seconds (5 minutes = 300 seconds)
let timeRemaining = 60;

// Select the timer display element
const timerDisplay = document.getElementById('timer');

// Function to start the countdown
function startCountdown() {
  const countdownInterval = setInterval(() => {
    // Calculate minutes and seconds
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;

    // Display the time remaining
    timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

    // Decrement time remaining
    timeRemaining--;

    // Check if time is up
    if (timeRemaining < 0) {
      clearInterval(countdownInterval); // Stop the timer
      window.location.href = 'index.html'; // Redirect to starting page
    }
  }, 1000); // Update every second
}

// Start the countdown when the page loads
window.onload = startCountdown;
