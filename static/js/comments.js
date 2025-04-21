document.addEventListener('DOMContentLoaded', function () {
  const container = document.getElementById('comments-container');
  const commentGroups = container.getElementsByClassName('comments-group');
  let currentIndex = 0;
  let interval;

  // Show first group initially
  commentGroups[0].classList.add('opacity-100');

  function showGroup(index) {
    for (let i = 0; i < commentGroups.length; i++) {
      commentGroups[i].classList.remove('opacity-100');
      commentGroups[i].classList.add('opacity-0');
    }

    commentGroups[index].classList.remove('opacity-0');
    commentGroups[index].classList.add('opacity-100');
  }

  function nextGroup() {
    currentIndex = (currentIndex + 1) % commentGroups.length;
    showGroup(currentIndex);
  }

  // Start the interval
  function startInterval() {
    interval = setInterval(nextGroup, 4000);
  }

  // Stop the interval
  function stopInterval() {
    clearInterval(interval);
  }

  // Add hover handlers
  container.addEventListener('mouseenter', stopInterval);
  container.addEventListener('mouseleave', startInterval);

  // Start initial interval
  startInterval();
}); 