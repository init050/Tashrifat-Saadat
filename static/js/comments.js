  document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('comments-container');
    const comments = Array.from(container.querySelectorAll('.comments-group'));
    const nextBtn = document.getElementById('next-comment');
    const prevBtn = document.getElementById('prev-comment');
    let currentIndex = 0;
    const totalComments = comments.length;


    function initializeComments() {
      comments.forEach((comment, index) => {
        comment.style.transition = 'all 0.5s ease';
        if (index === 0) {
          comment.style.transform = 'translateX(0)';
          comment.style.opacity = '1';
        } else {
          comment.style.transform = 'translateX(100%)';
          comment.style.opacity = '0';
        }
      });
    }

    initializeComments();

    function moveSlide(direction) {
      const current = comments[currentIndex];
      let nextIndex;
      
      if (direction === 'next') {
        nextIndex = (currentIndex + 1) % totalComments;
        comments[nextIndex].style.transform = 'translateX(100%)';
      } else {
        nextIndex = (currentIndex - 1 + totalComments) % totalComments;
        comments[nextIndex].style.transform = 'translateX(-100%)';
      }

      const next = comments[nextIndex];
      next.style.opacity = '0';

      requestAnimationFrame(() => {
        current.style.transform = direction === 'next' ? 'translateX(-100%)' : 'translateX(100%)';
        current.style.opacity = '0';

        next.style.transform = 'translateX(0)';
        next.style.opacity = '1';
      });

      currentIndex = nextIndex;
    }

    nextBtn.addEventListener('click', () => moveSlide('next'));
    prevBtn.addEventListener('click', () => moveSlide('prev'));

    let touchStartX = 0;
    container.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    });

    container.addEventListener('touchend', e => {
      const touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;
      
      if (Math.abs(diff) > 50) {
        if (diff > 0) {
          moveSlide('next');
        } else {
          moveSlide('prev');
        }
      }
    });
  });