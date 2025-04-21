document.addEventListener('DOMContentLoaded', function () {
  const container = document.getElementById('gallery-container');
  const images = container.getElementsByClassName('gallery-image');
  let currentIndex = 0;

  function showImage(index) {
    for (let i = 0; i < images.length; i++) {
      images[i].classList.remove('opacity-100');
      images[i].classList.add('opacity-0');
    }

    images[index].classList.remove('opacity-0');
    images[index].classList.add('opacity-100');
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  }
  setInterval(nextImage, 4000);
});
